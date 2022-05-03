#Advertising.csv : 여러 매체를 통한 광고비 판매량 추정치 얻기

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tests.frame.methods.test_sort_values import ascending
plt.rc('font', family = 'malgun gothic')

advdf = pd.read_csv("../testdata/Advertising.csv", usecols = [1, 2, 3, 4])
print(advdf.head(3), advdf.shape) #(200, 4)

print('상관계수(r) : ', advdf.loc[:, ['sales', 'tv']].corr()) #sales와 tv의 상관관계를 알기
#상관계수(r) : sales        tv
#   sales  1.000000  0.782224
#   tv     0.782224  1.000000
print('상관계수(r) : ', advdf.loc[:, ['sales', 'newspaper']].corr())
#상관계수(r) : sales  newspaper
#sales      1.000000   0.228299
#newspaper  0.228299   1.000000
print('상관계수(r) : ', advdf.loc[:, ['sales', 'radio']].corr())
#상관계수(r) : sales     radio
#    sales  1.000000  0.576223
#    radio  0.576223  1.000000
print("-------------------------")

#tv가 제일 높으니 tv로 선형회귀
lm = smf.ols(formula = 'sales ~ tv', data = advdf).fit()
print(lm.summary())
#Prob (F-statistic):1.47e-42
#R-squared:0.612

print('설명력 : ', lm.rsquared) #0.611875050850071
print('p값 : ', lm.pvalues) #1.467390e-42

#위 값을 구하는 이유는 미지의 독립변수 값에 대한 예측 결과를 얻기 위해서
#인과관계가 있고 상관관계가 있을 때 좋은 모델이 만들어 진다 -> y값이 잘 만들어진다

#시각화
"""
plt.scatter(advdf.tv, advdf.sales)
plt.xlabel('tv')
plt.ylabel('sales')
x = pd.DataFrame({'tv' : [advdf.tv.min(), advdf.tv.max()]})
y_pred = lm.predict(x)
plt.plot(x, y_pred, 'r')
plt.show()
"""

#미지의 TV 광고비에 따른 상품 판매량 예측
x_new = pd.DataFrame({'tv' : [220.12, 55.66, 10]})
pred_new = lm.predict(x_new)
print('TV광고비에 따른 판매량 추정은 : ',pred_new.values) 
#[17.49635884  9.67848296  7.50795995]
print('------------------------------------------')

print(advdf.corr()) #sales와의 상관관계 : tv -> radio -> newspaper
lm_mul = smf.ols(formula = 'sales ~ tv + radio + newspaper', data=advdf).fit() #추론 통계의 샘플데이터 작업 중
print(lm_mul.summary())
#Prob (F-statistic):1.58e-96
#Adj. R-squared:0.896

#                coef    std err          t      P>|t|      [0.025      0.975]
#------------------------------------------------------------------------------
#Intercept      2.9389      0.312      9.422      0.000       2.324       3.554
#tv             0.0458      0.001     32.809      0.000       0.043       0.049
#radio          0.1885      0.009     21.893      0.000       0.172       0.206
#newspaper     -0.0010      0.006     -0.177      0.860      -0.013       0.011

#newspaper의 p-value는 0.860으로 0.05보다 매우 크므로 독립 변수에서 제외하는 것을 생각해볼 필요가 있다


lm_mul = smf.ols(formula = 'sales ~ tv + radio', data=advdf).fit() #newspaper의 pvalue가 너무 높으니 제외하고 작업
print(lm_mul.summary())
#Prob (F-statistic):4.83e-98
#Adj. R-squared:0.896
#독립변수 newspaper가 없더라도 결정계수에는 큰 차이가 없는 것을 보니 모델의 성능에 큰 영향을 주지 않는 변수이다 

#tv만 사용했을 때 AIC = 1042, tv + radio + newspaper AIC = 780.4 tv + radio AIC = 778.4로
#tv와 radio만 사용했을 때가 제일 최상이다

#새로운 독립변수 값으로 sales를 예측해서 추정치를 얻기
x_new2 = pd.DataFrame({'tv' : [220.12, 55.66, 10], 'radio' : [30.3, 40.4, 50.5]})
pred_new2 = lm.predict(x_new2)
print('2개의 독립변수로 확인한 TV광고비에 따른 판매량 추정은 : ',pred_new2.values)
#[17.49635884  9.67848296  7.50795995]
print('------------------------------------------')



#*** 선형회귀분석의 기존 가정 충족 조건 ***
#. 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
#. 정규성 : 잔차항이 정규분포를 따라야 한다.
#. 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
#. 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
#. 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.

#잔차항 구하기(실제값 - 예측값)
fitted = lm_mul.predict(advdf.iloc[:, 0:2]) #tv와 radio 칼럼만 이용해서 예측값 구하기 위해 0열부터 1열까지만
#print(advdf.iloc[:, 0:2])
print(fitted) #예측값

#잔차 구하기
residual = advdf['sales'] - fitted
print(residual) #실제값 - 예측값
print(np.mean(residual)) #5.511147094239277e-15 실제값과 예측값은 큰 차이가 없다


#선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
#예측값과 잔차의 분포가 유사하다

import seaborn as sns
sns.regplot(fitted, residual, lowess = True, line_kws = {'color' : 'red'}) #선형회귀 모델의 적합성을 그릴 때 사용 - 잔차의 추세선을 시각화
#최저모델을 취화? 25분
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='gray') #예측값의 최소값과 예측값의 최대값을 걸어둠 - 평균값
#plt.show()
#위의 모델은 선형성을 만족하지 못함 - 데이터의 산포도를 따라서 선이 비선형으로 이동
#위와 같은 상황일 때는 다항회귀(비선형) 모델을 추천한다. - PolynomialFeatures
print('------------------------------------------')



#정규성 : 잔차가 정규분포를 따르는지 확인 Q-Q plot를 사용
import scipy.stats
sr = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3, 3], [-3, 3], '--', color='gray')
#plt.show()
#잔차가 정규성을 만족하지 못함 - 산포되어 있는 데이터가 선의 범위를 넘어감
#정규성을 만족하지 않음 : 데이터에 대해 표준화, 정구화, log를 씌우는 등의 작업을 시도한다

print('shapiro test : ', scipy.stats.shapiro(residual))
#ShapiroResult(statistic=0.9180378317832947, pvalue=4.190036317908152e-09)
#shapiro에서는 pvalue가 0.05보다 커야된다.
#pvalue가 0.05보다 작으므로 정규성을 만족하지 못함 
print('------------------------------------------')



#독립성 : 잔차가 자기상관을 따르는지 확인 - 따르면 안 됨. 독립적이어야 한다.
#독립변수의 값이 서로 관련되지 않아야 한다.
#Durbin-Watson:2.081 -> 0~4까지의 값을 가질 때 2에 가까워야 독립성이 있다.
#0에 가까우면 음의 자기상관 4에 가까우면 양의 자기상관을 가진다. -> 독립적이지 않다.



#등분산성 : 잔차의 분산이 일정해야한다
#데이터가 선을 따라가는 것이 제일 좋다. 선이 휘어지는 것은 패턴이 있다 - 등분산성을 만족하지 못 한다
sr = scipy.stats.zscore(residual)
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws = {'color' : 'red'})
#plt.show()
#등분산성 만족 못함 : 비선형인지 확인, 이상값 확인, 정규성 확인
#정규성은 만족하나 등분산성은 만족하지 못한 경우 가중회귀분석(weighted regression)을 한다



#다중공산성 : 독립변수들 간에 상관관계가 강하면 안 된다.
#독립변수는 종속변수와 강해야 한다.
from statsmodels.stats.outliers_influence import variance_inflation_factor

#VIF(분산 팽창 계수)값 확인 - 10을 넘으면 다중공산성을 의심
print(variance_inflation_factor(advdf.values, 1)) #tv   12.570312383503682  10을 넘으니 의심할 필요가 있음
print(variance_inflation_factor(advdf.values, 2)) #radio   3.1534983754953845

vifdf = pd.DataFrame() #DataFrame로 확인하기
vifdf['vif_value'] = [variance_inflation_factor(advdf.values, i) for i in range(1, 3)]
print(vifdf)
#   vif_value
#0  12.570312
#1   3.153498
#tv는 다중곤산성이 높으므로 의심을 해봐야 한다
print()



#아웃라이어인 이상치를 생각해서 확인하기
#극단치(이상치) 확인 - Cook's distance
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm_mul).cooks_distance #극단값을 나타내는 지표 반환
print(cd.sort_values(ascending=False).head())


import statsmodels.api as sm
sm.graphics.influence_plot(lm_mul, criterion = 'cooks')
plt.show()

print(advdf.iloc[[130, 5, 35, 178, 126]])
#해당 값들을 제외하면 더 좋은 값이 나올 수도 있다




