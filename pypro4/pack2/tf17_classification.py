from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, RMSprop, SGD
#SGD는 확률적 계산밥에서 모멘텀 문제가 있음 경사가 두 번 꺾일 때 최소값 전의 꺾임에서 구분하지 못 하는 것
#제일 좋은 모델은 Adam

x_data = [[1,2],[2,3],[3,4],[4,3],[3,2],[2,1]] #matrix
y_data = [[0],[0],[0],[1],[1],[1]] #vector or matrix

#Sequential api로 실습 function api도 해볼거

#model = Sequential([
#    Dense(units = 1, input_dim = 2), #input_shape = (2,)로 쓸 수도 있다
#    Activation('sigmoid') #0~1까지의 2항분류 odds분류로 로짓 변환을 함. 
#])

#위의 방법도 사용하지만 아래의 방법을 더 많이 사용함
model = Sequential()
model.add(Dense(units = 1, input_dim = 2, activation = 'sigmoid')) #노드는 하나, 입력은 두 개, 출력은 sigmoid 이항 분류니 하나
model.compile(optimizer = Adam(learning_rate = 0.1), loss = 'binary_crossentropy', metrics = ['accuracy'])
#Adam(learning_rate = 0.1) 최적의 minimizer를 찾기 위해 Adam을 사용하고 학습율은 0.1씩 진행하는 것
#loss = 'binary_crossentropy' activation이 sigmoid이면 무조건 사용

print(model.summary())

model.fit(x = x_data, y = y_data, epochs = 100, batch_size = 1, verbose = 0) #제대로 하려면 x, y를 train_data로 줘야함
#훈련된 모델을 평가할 떄는 train으로 훈련하고 test로 확인
m_eval = model.evaluate(x = x_data, y = y_data, batch_size = 1, verbose = 1)
print(m_eval)
#loss: 0.0226(0에 가까울 수록 좋다) - accuracy: 1.0000(1에 가까울 수록 좋다) 둘은 반비례 관계에 놓여있다


#새로운 값으로 결과 얻기
import numpy as np
new_data = [[1, 2], [10, 7]]
pred = model.predict(new_data , batch_size = 1, verbose = 1)
print('예측 결과 : ', pred)
print('예측 결과 : ', np.squeeze(np.where(pred > 0.5, 1, 0))) #보기 편하게 pred값을 0.5를 기준으로 이항으로 분류한다
#np.squeeze 차원을 떨어뜨리는 것
print('예측 결과 : ', [1 if i > 0.5 else 0 for i in pred]) #또는 이런식으로도 가능 ndarray 형식으로 나옴
print('---------------------------------------------------')
#예측 결과 :  [[0.03481552]
# [0.99994236]]
#예측 결과 :  [[0]
# [1]]
#예측 결과 :  [0, 1]


#function api
from keras.layers import Input
from keras.models import Model

inputs = Input(shape = (2,))
output = Dense(units = 1, activation = 'sigmoid')(inputs)
model2 = Model(inputs, output)

model2.compile(optimizer = Adam(learning_rate = 0.1), loss = 'binary_crossentropy', metrics = ['accuracy'])
#print(model.summary())

model2.fit(x = x_data, y = y_data, epochs = 100, batch_size = 1, verbose = 0) #제대로 하려면 x, y를 train_data로 줘야함
m_eval2 = model2.evaluate(x = x_data, y = y_data, batch_size = 1, verbose = 1)
print(m_eval2)










