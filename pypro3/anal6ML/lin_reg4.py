#iris dataset으로 선형회귀분석을 시도
#상관관계가 약한 경우와 강한 경우로 분석 모델을 작성해 비교해 보기

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

iris = sns.load_dataset('iris')
#print(iris.head(3), iris.shape) #(150, 5)
#print(iris.corr(method='pearson'))

#단순 선형회귀
#1. 상관관계가 약한 두 변수
#                sepal_width
#sepal_length    -0.117570

result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()
print(result1.summary()) #Prob (F-statistic): 0.152  R-squared: 0.014
#pvalue가 0.05보다 커서 무의미하다. t값이 작으니 p값이 커짐. 데이터가 퍼져있다
#종속변수에 대해 독립변수의 설명력은 0.014밖에 안 된다
#데이터가 분산되어 있어 회귀선은 우연히 만들어진 선이다

print('R squared : ', result1.rsquared) #R squared :  0.013822654141080859
#print('p-values : ', result1.pvalues) ??
print('p-values : ', result1.pvalues[1]) #p-values :  0.15189826071144785

#1모델은 의미가 없는 모델이다
print('실제 값 : ', iris.sepal_length[:5].values) #실제 값 :  [5.1 4.9 4.7 4.6 5. ]
print('예측 값 : ', result1.predict()[:5]) #예측 값 :  [5.74445884 5.85613937 5.81146716 5.83380326 5.72212273]
#
print('---------------------------------------')



#2. 상관관계가 강한 두 변수
#                sepal_width
#petal_length    0.871754
result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()
print(result2.summary()) #Prob (F-statistic):1.04e-47  R-squared:0.760
print('R squared : ', result2.rsquared) #R squared :  0.7599546457725151
print('p-values : ', result2.pvalues[1]) #p-values :  1.0386674194499307e-47 <0.05 의미가 있는 모델이다

#1모델은 의미가 있는 모델이다
print('실제 값 : ', iris.sepal_length[:5].values) #실제 값 :  [5.1 4.9 4.7 4.6 5. ]
print('예측 값 : ', result2.predict()[:5]) #예측 값 :  [4.8790946  4.8790946  4.83820238 4.91998683 4.8790946 ]

#petal_length는 sepal_length를 76%만큼 설명하고 있다
#즉 petal_length로 sepal_length를 76%만큼 예측할 수가 있다
print('---------------------------------------')

#새로운 값(petal_length)으로 미지의 sepal_length값 얻기
new_data = pd.DataFrame({'petal_length':[1.1, 0.5, 5.0]})
y_pred = result2.predict(new_data)
print('예측 결과 : ', y_pred.values) #[4.75641792 4.51106455 6.3512148 ]
print('---------------------------------------')




#다중 선형회귀 : 독립변수 복수
#                sepal_width    petal_length    petal_width
#sepal_length    -0.117570        0.871754        0.817941
#print(iris.corr(method='pearson'))
#result3 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width + sepal_width', data = iris).fit()
#print(result3.summary())

#세 개의 변수 모드 p값이 0.05보다 작아 유의하다
#독립변수가 2개 이상이 되면 Adj. R-squared 수정된 결정계수로 확인 0.856
#성능 파악하기 위해 독립변수 하나, 둘, 세개 썻을 때의 AIC 값을 확인해야 한다.


#종속변수를 제외한 독립변수의 갯수가 무수히 많을 때 변수의 개수를 줄여나가고 선택하는 것이 중요
#또한 다른 파일들에 있는 변수들을 머지하여 데이터를 분석할 수도 있다

#여러 개의 독립 변수를 사용할 때 R에서는 .을 사용했지만 python에서는 join을 사용한다
column_select = "+".join(iris.columns.difference(['sepal_length', 'species'])) 
#빠져야 될 변수만 적어줌. sepal_length는 종속변수, species는 정수도 아니고 종속 변수에 영향을 주는 독립 변수도 아니기 때문에 

#print(column_select) #petal_length+petal_width+sepal_width

result3 = smf.ols(formula = 'sepal_length ~ ' + column_select, data = iris).fit()
print(result3.summary())







