#선형/비선형(다항)회귀 모델 : boston_housing dataset - 살짝 비선형을 이루고 있어서 사용 
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')

df = pd.read_csv("../testdata/housing.data", header=None, sep="\s+")
df.columns = ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat', 'medv']
print(df.head(3), df.shape)
print(df.corr()['medv']) #lstat(하위계층 비율)와 medv(집값)의 상관관계 : -0.737663
#집값을 예측할 거니 medv를 기준으로

x = df[['lstat']].values
y = df['medv'].values

print(x[:3],'\n',y[:3]) #x는 matrix, y는 vector

model = LinearRegression()

#다항특성
quad = PolynomialFeatures(degree=2) #2차 열이 2개
cubic = PolynomialFeatures(degree=3) #3차 열이 3개
x_quad=quad.fit_transform(x)
x_cubic=cubic.fit_transform(x)

print(x_quad[:2])
#[[ 1.      4.98   24.8004]
# [ 1.      9.14   83.5396]]

print(x_cubic[:2]) #열의 갯수가 3개니 overfitting의 확률이 높다
#[[  1.         4.98      24.8004   123.505992]
# [  1.         9.14      83.5396   763.551944]]


#단순회귀
model.fit(x, y)
x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
y_lin_fit = model.predict(x_fit) #시각화 하려고 만듬
print('단순회귀 예측값 : ', y_lin_fit[:3]) #[32.9102555  31.96020614 31.01015679]

model_r2 = r2_score(y, model.predict(x))
print('단순회귀 성능점수 : ', model_r2) #0.5441462975864799  54%의 설명력을 가지고 있다



#다항회귀 : 2차
model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y, model.predict(x_quad))
print('다항회귀 2차(quad) : ', q_r2) #0.6407168971636611



#다항회귀 : 2차
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('다항회귀 3차(cubic) : ', c_r2) #0.6578476405895719



#시각화
plt.scatter(x, y, c='gray', label='train data')
plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear(dim=1), $R^2=%.2f$'%model_r2, c='b', lw=3)
plt.plot(x_fit, y_quad_fit, linestyle='-', label='quad(dim=2), $R^2=%.2f$'%q_r2, c='r', lw=3)
plt.plot(x_fit, y_cubic_fit, linestyle='--', label='cubic(dim=3), $R^2=%.2f$'%c_r2, c='y', lw=3)
plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()







