#다중선선형회귀 : 주식 데이터로 회귀모델 작성. 하루 전 데이터로 다음 날 종가 예측
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

xy = np.loadtxt("../testdata/stockdaily.csv", delimiter=",", skiprows = 1)
print(xy[:2], len(xy))

#데이터의 성격이 다른 하나가 있다 데이터의 가공이 필요함
scaler = MinMaxScaler(feature_range=(0, 1)) #정규화
xy = scaler.fit_transform(xy)
print(xy[:2], len(xy)) #데이터가 0~1범위 내에 들어옴

x_data = xy[:, 0:-1] #Open, High, Low, Volume : feature
y_data = xy[:, [-1]] #Close : label
print(x_data[:2])
print(y_data[:2])
print('-----------------------------------')

print(x_data[0], y_data[0])
print(x_data[1], y_data[1])
print('-----------------------------------')

#전처리
#오늘 종가를 없애고 다음 날 종가 데이터와 오늘 주식 데이터의 행을 맞춰줌
x_data = np.delete(x_data, -1, 0) #마지막 행 삭제
y_data = np.delete(y_data, 0) #0번째 행 삭제
print(x_data[0], y_data[0])
print(x_data[1], y_data[1])
print('-----------------------------------')
#[0.97333581 0.97543152 1.         0.11112306] [0.98831302]
#[0.95690035 0.95988111 0.9803545  0.14250246] [0.97785024]

#[0.97333581 0.97543152 1.         0.11112306] 0.9778502390712853
#[0.95690035 0.95988111 0.9803545  0.14250246] 0.9664546348847527
#다음과 같이 오늘 종가 데이터를 지우고 다음 날 종가 데이터를 가져옴
#오늘 주식 데이터를 가지고 다음 날 종가 데이터를 맞추는 알고리즘을 짜는 것


model = Sequential()
#덴스만이 가능 layer는 한 개만 사용
model.add(Dense(units = 1, input_dim = 4, activation='linear')) #데이터의 정확도가 떨어지면 layer의 수를 늘리면 됨

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(x_data, y_data, epochs = 100, verbose = 0)
print('evaluate : ', model.evaluate(x_data, y_data))
#loss는 점점 줄어듬
print('-----------------------------------')

print(x_data[10]) #데이터가 벡터로 되어있음 matrix로 바꿔줘야됨
test = x_data[10].reshape(-1,4) #2차원으로 바꿔줌
print('실제값 : ', y_data[10]) #0.900384
print('예측값 : ', model.predict(test).flatten()) #[0.8672385]
print('-----------------------------------')

pred = model.predict(x_data)
from sklearn.metrics import r2_score
print('r2_score : ', r2_score(y_data, pred)) #0.960432  꽤나 높음 과적합 의심스러움

#plt.plot(y_data, 'b')
#plt.plot(pred, 'r--')
#plt.show()
#과적합이 의심스러우니 train, test로 나눠봄 - 데이터가 30개면 할 필요가 없다


#과적합 방지를 목적으로 데이터를 train / test로 분리하여 작업
#R에서는 train/test split이 없으니 r처럼 해봄
train_size = int(len(x_data) * 0.7) 
test_size = len(x_data) - train_size
print(train_size, test_size) #511 220로 나눔
print('-----------------------------------')
x_train, x_test = x_data[0:train_size], x_data[train_size:len(x_data)]
#x_data의 0번째 부터 511번째까지와 511번째부터 끝까지를 나눔
print(x_data[:2])#잘 나눠졌는지 봐야하니까
print('-----------------------------------')
print(x_train[:2], x_train.shape, ' ', x_test[:2], x_test.shape) 
print('-----------------------------------')
y_train, y_test = y_data[0:train_size], y_data[train_size:len(x_data)]
print(y_train[:2], y_train.shape, ' ', y_test[:2], y_test.shape) 
print('-----------------------------------')

#현재 연습하는 stockdaily.csv 데이터는 시계열 데이터라 섞이면 시간 순서가 복잡해짐
#순서가 있는 데이터는 섞으면 안 된다
#from sklearn.model_selection import train_test_split
#a, b, c, d = train_test_split(x_data, y_data, shuffle = True) #shuffle에 False로 주어 suffle값을 안 줄 수 있다 





model2 = Sequential()
#덴스만이 가능 layer는 한 개만 사용
model2.add(Dense(units = 1, input_dim = 4, activation='linear')) #데이터의 정확도가 떨어지면 layer의 수를 늘리면 됨

model2.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model2.fit(x_train, y_train, epochs = 100, verbose = 0) #학습은 train으로
print('evaluate : ', model2.evaluate(x_test, y_test))
#loss는 점점 줄어듬
print('-----------------------------------')

print(x_test[10]) #데이터가 벡터로 되어있음 matrix로 바꿔줘야됨
test = x_test[10].reshape(-1,4) #2차원으로 바꿔줌
print('실제값 : ', y_test[10]) #0.1243311
print('예측값 : ', model2.predict(test).flatten()) #[0.11142521]
print('-----------------------------------')

pred2 = model2.predict(x_test)
print('split after r2_score : ', r2_score(y_test, pred2)) #0.78092  나누고 보니 과적합이 의심되지 않음.
print('-----------------------------------')


#fit(학습) 도중에 검증도 함께 하고자 할 경우, train data를 다시 분리해 validation data를 운영할 수 있다
#과적합 방지를 목적으로    이래도 과적합이 발생하면 DL에서 따로 하는 방법이 있음

model3 = Sequential()
#덴스만이 가능 layer는 한 개만 사용
model3.add(Dense(units = 1, input_dim = 4, activation='linear')) 

model3.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model3.fit(x_train, y_train, epochs = 100,
           validation_split = 0.15, verbose = 0) #train을 3:7비율로 나눔
print('evaluate : ', model3.evaluate(x_test, y_test))

pred3 = model3.predict(x_test)
print('split after r2_score : ', r2_score(y_test, pred3))

plt.plot(y_test, 'b')
plt.plot(pred3, 'r--')
plt.show()





