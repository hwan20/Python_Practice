#회귀분석방법 확인 : 맛보기
#잔차 제곱합이 최소가 되는 추세선을 만들고 이를 통해 독립변수(feature)가
#종속변수(label or calss)에 얼마나 영향을 주는지 인과관계를 분석 
#두 개 이상의 변수는 상관관계가(피어슨 상관계수 0.25이상) 있어야 하고
#나아가서는 인과관계가 있어야 한다.

#선형회귀 **

#정량적인 모델을 생성

from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)

#모델 맛 보기1 : make_regression을 사용. model 생성 X
x, y, coef = make_regression(n_samples = 50, n_features = 1, bias = 100, coef = True)
print(x)
print(y)
print(coef) #기울기 : 89.47430739278907(seed에 따라서 바뀌는 동적인 값), 절편 : 100  y = wx + b
print('예측값 : ', coef * -1.70073563 + 100) #-52.17214255248879
print('실제값 : ', -52.17214291) #-52.17214291

print('예측값 : ', coef * -0.67794537 + 100) #39.34130756910188
print('실제값 : ', 39.34130801) #39.34130801
#값이 같을 수 밖에 없다 make_regression은 그런 함수임

#참고 : 머신러닝은 귀납적 추론방식을 따른다

print('---------------------------------------')
#모델 맛 보기2 : LinearRegression을 사용. model 생성 O
from sklearn.linear_model import LinearRegression
model = LinearRegression()

xx = x
yy = y

fit_model = model.fit(xx, yy) #학습 데이터로 모형 추정(training) : 절편과 기울기를 얻음
print('slope : ', fit_model.coef_) #89.47430739  절편 100일 때 기울기 make_regression과 같다
print('bias : ', fit_model.intercept_) #100.0   y = 89.47430739 * x + 100
print('모델이 예측한 값(수식을 사용) : ', 89.47430739 * -1.70073563 + 100) #-52.172142547745324
y_new = fit_model.predict(xx[[0]]) #입력이 2차원이라 [[]] 사용 위에서 매트릭스를 사용했기 때문
#print('모델이 예측한 값(method 사용) : ', y_new) #-52.17214291
print('모델이 예측한 값(method 사용) : ', y_new[0]) #차원을 떨어트려 주고 싶을 때

#우리가 알고 싶은 것은 어떠한 미지의 값에 대한 예측 값
print('미지의 x에 대한 새로운 예측값 : ', fit_model.predict([[66]]))#6005.30428792


print('---------------------------------------')
#모델 맛 보기3 : ols를 사용. model 생성 O
import statsmodels.formula.api as smf
import pandas as pd
x1 = xx.flatten() #차원 축소
y1 = yy
print(x1.shape, ' ', y.shape) #(50,)   (50,)

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
print(df.head(3))

model2 = smf.ols(formula = 'y1 ~ x1', data = df).fit()
print(model2.summary())
#Intercept : 100.0000   slope : 89.4743

#예측값 확인 함수
print(x1[:2])
new_df = pd.DataFrame({'x1':[-1.70073563, -0.67794537]}) #기존 자료로 예측값 확인
new_pred = model2.predict(new_df)
print('모델이 예측한 값(method) : \n', new_pred)
#0   -52.172143  1    39.341308
print('----------------------------')

new2_df = pd.DataFrame({'x1':[7, -2.345]}) #새로운 자료로 예측값 확인
new2_pred = model2.predict(new2_df)
print('모델이 예측한 새로운 값(method) : \n', new2_pred)
#0    726.320152  1   -109.817251






