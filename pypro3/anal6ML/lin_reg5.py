#선형회귀 : mtcars dataset 으로 선형회귀 분석 시도

import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
#print(mtcars.columns) #['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
#print(mtcars.describe())
print(mtcars.corr()) #연비와 차체무게, 마력수만 필요
print(np.corrcoef(mtcars.hp, mtcars.mpg)) #연비와 마력수  -0.77616837  독립변수가 높을 수록 종속변수가 낮아지는 음의 상관관계
print(np.corrcoef(mtcars.wt, mtcars.mpg)) #차체와 마력수  -0.86765938  음의 상관관계가 높다

#시각화
"""
plt.scatter(mtcars.hp, mtcars.mpg)
plt.xlabel('마력수')
plt.ylabel('연비') #mtcars.hp
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1) #연비와 마력수의 상관관계를 1차원 시각화 해서 보기 위해 
plt.plot(mtcars.hp, mtcars.hp * slope + intercept, 'r') #y값을 알기 위한 기울기 slope와 절편 intercept
plt.show()
"""

#모델은 만들어 졌으니 ML을 만들기
#단순 선형회귀
result = smf.ols('mpg ~ hp', data=mtcars).fit()
#print(result.summary())
#Prob (F-statistic):1.79e-07  p값은 0.05보다 작으니 모델은 유의하다
#R-squared:0.602  60.2% 만큼 설명됨
#독립변수가 하나밖에 없으니 다른 것은 안 봐도 됨

#summary를 반만 보고 싶을 때
print(result.summary().tables[0])
print(result.summary().tables[1])

print('마력수 110에 대한 연비 예측 : ', -0.0682 * 110 + 30.0989) #coef.hp(기울기)   coef.Intercept(절편)
print('마력수 50에 대한 연비 예측 : ', -0.0682 * 50 + 30.0989)
#마력수 110에 대한 연비 예측 :  22.5969
#마력수 50에 대한 연비 예측 :  26.6889
#연비는 마력수에 반비례 한다
#100%확실하지는 않다. 연비를 정하는 기준에는 마력수 외에 무게, 연식 등등 영향을 주는 것은 많으니까.
print('--------------------------------------')


#다중 선형회귀
result2 = smf.ols('mpg ~ hp + wt', data=mtcars).fit()
print(result2.summary())
#Prob (F-statistic):9.11e-12   유의하다
#Adj. R-squared:0.815  81.5의 설명력
#hp            -0.0318      0.009     -3.519      0.001      -0.050      -0.013
#wt            -3.8778      0.633     -6.129      0.000      -5.172      -2.584
#두 변수 다 설명력이 있다

print('마력수 110 + 차체 무게 5t 에 대한 연비 예측 : ', (-0.0318 * 110) + (-3.8778 * 5) + 37.2273) #coef.hp(기울기)   coef.Intercept(절편)
print('마력수 50 + 자체 무게 10t 에 대한 연비 예측 : ', (-0.0318 * 50) + (-3.8778 * 10) + 37.2273)
#마력수 110 + 차체 무게 5t 에 대한 연비 예측 :  14.3403
#마력수 50 + 자체 무게 10t 에 대한 연비 예측 :  -3.1407000000000025
#예측 값이라 정확하지 않다


print('추정치 구하기 : predict')
result3 = smf.ols('mpg ~ wt', data=mtcars).fit()
print('결정계수 r : ', result3.rsquared) #0.7528327936582646
print('p-value : ', result3.pvalues[1]) #1.2939587013505116e-10 < 0.05 유의하다

pred = result3.predict() #학습 데이터로 예측
print(pred) #모든 자동차 데이터에 따른 연비값

#하나만 보기    여러 개를 보기 위해서는 [:n]
print(mtcars.mpg[0]) #실제 값 : 21.0
print(pred[0]) #예측 값 : 23.282610646808624


#DataFrame에 실제 값과 예측 값 담기
data = {
    'mpg' : mtcars.mpg,
    'mpg_pred' : pred
}

df = pd.DataFrame(data)
print(df)


#새로운 차체 무게를 입력받아 연비 예측하기
#mtcars.wt = float(input('차체 무게 : '))
#new_pred = result3.predict(pd.DataFrame(mtcars.wt))
#print('차체 무게 : {}일 때 예상 연비는 {}이다.'.format(mtcars.wt[0], new_pred[0]))


#차체 무개가 여러 개일 때는
new_wt = pd.DataFrame({'wt':[6, 3, 1]})
new_pred2 = result3.predict(pd.DataFrame(new_wt))
#print(new_wt.values[0])
print('예상 연비 : \n', np.round(new_pred2.values,2)) #[ 5.22 21.25 31.94]
print('차체 무게 : {}, {}, {} 일 때 예상 연비는 {}, {}, {} 이다.'.format(new_wt.values[0], new_wt.values[1], new_wt.values[2],
                                                            new_pred2.values[0], new_pred2.values[1], new_pred2.values[2]))





