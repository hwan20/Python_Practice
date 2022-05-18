
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

#XOR게이트 논리 모델을 생성 후 처리
#1. 데이터 셋 생성
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
print(x) #feature
print(y) #label(class)

#model = Sequential([
#    Dense(input_dim = 2, units = 1), #입력은 2개, 출력은 1개
#    Activation('sigmoid')
#])

#아래와 같이 작성할 수도 있음 위와 같음
#model = Sequential()
#model.add(Dense(5, input_dim = 2)) #units = 5 생략함
#model.add(Activation('relu')) #중간 layer에서 sigmoid를 사용해도 되지만 성능이 좋지 않으니 relu를 사용
#model.add(Dense(1)) #5개가 입력되어 출력은 하나로, 입력은 안 써도 됨
#model.add(Activation('sigmoid')) #마지막에 이진 분류라서 sigmoid를 사용
#노드는 하나 원하는 출력은 XOR이라 정확도가 떨어짐

#아래는 위와 같다
model = Sequential()
model.add(Dense(units = 5, input_dim = 2, activation = 'relu'))
model.add(Dense(units = 5, activation = 'relu'))
model.add(Dense(units = 5, activation = 'relu'))
model.add(Dense(units = 1, activation = 'sigmoid')) #relu에서 나오는 출력은 5개니 안 써도 된다

#편한 걸로 작성해도 된다. layer가 늘어날 때마다 코드 늘려주면 됨
#model.add(Dense(units = 5, input_dim = 2, activation = 'relu'))
#model.add(Dense(units = 5, activation = 'relu'))
#model.add(Dense(units = 5, activation = 'relu'))
#model.add(Dense(units = 5, activation = 'relu'))
#model.add(Dense(units = 1, activation = 'sigmoid'))

#units수와 layer수는 정해지지 않음 판별해서 정해줘야 함

#모델 학습과정 설정 (컴파일)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(x, y, epochs = 100, batch_size = 1, verbose = 0) 
#history = model.fit(x, y, epochs = 100, batch_size = 1, verbose= 0)
#batch_size = 1은 1번 학습할 때마다 답을 맞춰줌. 크면 속도가 빠름. 그렇다고 너무 많이 주면 안 좋음
loss_metrics = model.evaluate(x, y)
print('loss_metrics : ', loss_metrics)

#pred = model.predict(x)
pred = (model.predict(x) > 0.5).astype('int32')
#print('예측결과 : ', pred)
print('예측결과 : ', pred.flatten()) #차원을 떨어트림 1차원 벡터

#epochs = 1일때 예측 결과의 정확도가 좋지 않음

#print('history : ', history.history)
#print('loss : ', history.history['loss'])
#print('acc : ', history.history['accuracy'])
#print('--------------------------------------')

#학습 진행 중 loss, acc를 시각화
#import matplotlib.pyplot as plt
#plt.plot(history.history['loss'], label = 'train loss')
#plt.plot(history.history['accuracy'], label = 'train accuracy')
#plt.xlabel('epochs')
#plt.legend(loc='best')
#plt.show()


print(model.layers) #모델층의 객체를 확인 가능
print(model.summary())
print('--------------------------------------')


print(model.weights)






