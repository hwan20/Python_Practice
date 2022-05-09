#선형회귀 모델을 다항회귀로 변환
#데이터가 선형가정이 어긋날 때(정규성 불만족)

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
#plt.scatter(x, y)
#plt.show()
#위의 데이터는 1차 함수로는 그릴 수 없다

#선형회귀모델 작성
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis]
print(x)

model = LinearRegression().fit(x, y)
ypred = model.predict(x)
print(ypred)

plt.scatter(x, y)
plt.plot(x, ypred, c='red')
plt.show()

#비선형 데이터인 경우에는 선형회귀모델로는 설명이 불완전하다
#그래서 좀 더 복잡한 모델이 필요
#모델에 유연성을 주기 위해 입력 데이터에 특징 열을 추가한다
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 2, include_bias = False) #degree - 열의 갯수 include_bias = False편향을 안 주겠다?
x2 = poly.fit_transform(x) #특징 행렬을 만듦
print(x2) #제곱을 해서 2열을 만듬

model2 = LinearRegression().fit(x2, y) #원래 값으로 모델을 만드는 것이 아니라 특징 행렬로 만든다
ypred2 = model2.predict(x2)
print(ypred2)

plt.scatter(x, y)
plt.plot(x, ypred2, c='blue')
plt.show()

#특징 열을 하나 추가시킴으로써 선형이었던 회귀선이 비선형인 회귀선으로 변화하였다
#이렇게 하면 원래의 데이터에 좀 더 가까운(편향이 적은) 모델을 만들 수 있다
#degree의 갯수가 많을 수록 편향이 적어진다. - 그렇다고 무조건 많이 주는 것이 좋은 것은 아니다 적당히 줘야 함
#즉, degree값이 얼마인가에 따라 다항식 모델의 성능이 달라진다











