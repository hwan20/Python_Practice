#sklearn 모듈이 제공하는 PolynomialFeatures를 사용하여 다항식 항 추가

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

x = np.array([258, 270, 294, 320, 342, 368, 396, 446, 480, 586])[:, np.newaxis]
print(x, x.shape)
y = np.array([236, 234, 253, 298, 314, 342, 360, 368, 391, 390])
print(y)

#plt.scatter(x, y)
#plt.show()
#선형이라고 하기에는 애매함


#선형 / 비선형 모델 작성 후 성능 비교
lr = LinearRegression() #선형회귀용
pr = LinearRegression() #다항회귀용
polyf = PolynomialFeatures(degree = 2)
x_quad = polyf.fit_transform(x)
print(x_quad)

#lr 선형
lr.fit(x, y)
x_fit = np.arange(250, 600, 10)[:, np.newaxis]
y_lin_fit = lr.predict(x_fit)
print('결과 예측(lr) : ', y_lin_fit)

#pr 비선형
pr.fit(x_quad, y)
y_quad_fit = pr.predict(polyf.fit_transform(x_fit))
print('결과 예측(pr) : ', y_quad_fit) #시각화를 위한 참고 자료


#시각화
plt.scatter(x, y, label = 'training ponts')
plt.plot(x_fit, y_lin_fit, label = 'linear fit', linestyle = '--', c='red')
plt.plot(x_fit, y_quad_fit, label = 'quadratic fit', linestyle = '-', c='blue')
plt.legend()
plt.show()
#선형인 회귀선보다는 잔차가 적지만 오버피팅을 조심해야 한다


#두 모델 성능 점수 확인
#딥러닝에서는 알아서 해줌;;
y_lin_pred = lr.predict(x)
y_quad_pred = pr.predict(x_quad)
print('MSE 비교 - 선형모델 : %.3f, 다항모델 : %.3f'%(mean_squared_error(y, y_lin_pred),
                                           mean_squared_error(y, y_quad_pred)))
print('결정계수 비교 - 선형모델 : %.3f, 다항모델 : %.3f'%(r2_score(y, y_lin_pred),
                                            r2_score(y, y_quad_pred)))

#MSE 비교 - 선형모델 : 570.885, 다항모델 : 58.294
#결정계수 비교 - 선형모델 : 0.831, 다항모델 : 0.983
#다항일 경우 R에서는 I() 함수를 사용
















