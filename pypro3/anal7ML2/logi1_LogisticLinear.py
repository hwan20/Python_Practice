#로지스틱 회귀분석(Logistic linear regression)
#분류 모델 : 이항분류가 기본
#독립변수 : 연속형   종속변수 : 범주형
#출력된 연속형 자료를 logit변환해 sigmoid function 함수로
#0~1사이의 실수 값이 나오도록 한 후 0.5를 기준으로 변환

#2진 분류시 logit() glm() 사용

import math

def sigmoidFunc(x):
    return 1 / (1+math.exp(-x))

#print(sigmoidFunc(3))
#print(sigmoidFunc(1))
#print(sigmoidFunc(-2))
#print(sigmoidFunc(-5))
#0.9525741268224334
#0.7310585786300049
#0.11920292202211755
#0.0066928509242848554
#0.5보다 크면 1로 작으면 0으로 바꾸는게 sigmoid function

#mtcars dataset으로 sigmoid function을 이용해 분류 작업을 진행

import statsmodels.api as sm

mtcarData = sm.datasets.get_rdataset('mtcars')
#print(mtcarData) #Dataset
#print(mtcarData.keys())
mtcars = mtcarData.data #mtcars 데이터 셋의 data를 가져옴
#print(mtcars.head())
#print(mtcars.am.unique()) #mtcars 데이터의 am은 1과 0밖에 없다. 수동이냐 자동이냐
mtcar = mtcars.loc[:,['mpg', 'hp', 'am']]

#연비와 마력수에 따른 변속기 분류 (수동이냐 자동이냐 나눔)

#모델 작성 방법1 : logit() 함수 사용

import statsmodels.formula.api as smf
import numpy as np
formula = 'am ~ mpg + hp' #종속변수 am, 독립변수 mpg와 hp
result = smf.logit(formula = formula, data = mtcar).fit() #학습시킬 때는 fit() 함수를 사용
print(result)
print(result.summary())
#No. Observations:32 관찰값
#                coef    std err          z      P>|z|      [0.025      0.975]
#------------------------------------------------------------------------------
#Intercept    -33.6052     15.077     -2.229      0.026     -63.156      -4.055
#mpg            1.2596      0.567      2.220      0.026       0.147       2.372
#hp             0.0550      0.027      2.045      0.041       0.002       0.108
#선형의 모양을 가져서 기울기가 있다
#P>|z| 의 값이 0.05보다 작아 의미가 있다

#print('예측값 : ', result.predict()) #[2.50047286e-01 2.50047286e-01 5.58034355e-01 ....

pred = result.predict(mtcar[:10])
#print('예측값 : ', pred.values)
print('예측값 : ', np.around(pred.values)) #반올림 해줌
print('실제값 : ', mtcar['am'][:10].values)

conf_tab = result.pred_table()
print('confusion matrix : \n', conf_tab)
#      예측값
#실제값 [[16.  3.]  TP, FN
#     [ 3. 10.]]  FP, TN

#빈도표를 이용하여 정확도를 구할 수가 있다
print('정확도 1 : ', (16+10) / len(mtcar)) #0.8125
print('정확도 2 : ', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar)) #0.8125


#위와 같지만 tensorflow에서는 conf_tab함수를 지원하지 않아 아래와 같이 구해야 한다
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print('정확도 3 : ', accuracy_score(mtcar['am'], np.around(pred2))) #0.8125


#logit 함수 내에서 odds비에 log를 씌우고 sigmoid 함수를 사용해서 연속형 데이터를 범주형 데이터로 변환함
#즉 연속형 실수를 logit 함수 내에서 계산하여 0.5이상은 1로 0.5미만은 0으로 분류해줌


#모델 작성 방법2 : glm() : generalized linear model(일반화된 선형 모델) 함수를 사용
#분류에서 선형 모델을 사용하여 범주형으로 변환

result2 = smf.glm(formula = formula, data=mtcar, family = sm.families.Binomial()).fit()#Binomial을 이용하여 이항 분포가 됨
print(result2)
print(result2.summary())
pred2 = result2.predict(mtcar[:10])
#print('예측값 : ', np.rint(pred2.values)) #둘 중 아무거나 사용 가능
print('예측값 : ', np.around(pred2.values)) 
print('실제값 : ', mtcar['am'][:10].values)
pred3 = result2.predict(mtcar)
print('정확도 : ', accuracy_score(mtcar['am'], np.around(pred3))) #0.8125
print('--------------------------------------------------------')

#새로운 연비와 마력 값으로 분류해 보기
#1. 기존 값을 수정해서 분류
newdf = mtcar.iloc[:4].copy()
print(newdf)
#                mpg   hp  am
#Mazda RX4      21.0  110   1
#Mazda RX4 Wag  21.0  110   1

newdf.mpg = [10, 30, 50, 5]
newdf.hp = [100, 130, 120, 50]
new_pred = result2.predict(newdf)
print('new_pred : ', new_pred.values)
print('new_pred : ', np.rint(new_pred.values))
print('--------------------------------------------------------')


#2. 새로운 값을 작성하여 분류
import pandas as pd
newdf2 = pd.DataFrame({'mpg' : [10, 30, 50, 5], 'hp' : [100, 130, 120, 50]})
new_pred2 = result2.predict(newdf2)
print('new_pred : ', new_pred2.values)
print('new_pred : ', np.rint(new_pred2.values))
print('--------------------------------------------------------')

#정확도가 100%가 나오면 데이터 모델로서의 가치가 없다 오버피팅되는 것
#100%에 조금 못 미치는 95% 이상의 값이 좋다







