#이항분류는 다항분류로도 처리 가능
#diabets dataset

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

dataset = np.loadtxt('../testdata/diabetes.csv', delimiter = ',')
print(dataset.shape)
print(dataset[:1])
print(set(dataset[:, -1])) #{0.0, 1.0}

#이항분류 : sigmoid
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(dataset[:, 0:8], dataset[:, -1],
                                                    test_size = 0.3, shuffle = True, random_state = 123) #마지막 데이터를 빼야됨
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(531, 8) (228, 8) (531,) (228,)

model = Sequential()
model.add(Dense(64, input_dim = 8, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['acc'])
model.fit(x_train, y_train, epochs = 100, batch_size = 32, verbose = 0, validation_split=0.2)
scores = model.evaluate(x_test, y_test)
print('이항분류 모델 성능 : %s : %.2f%%'%(model.metrics_names[1], scores[1] * 100)) #model.metrics_names[0]은 loss
print('이항분류 모델 성능 : %s : %.2f'%(model.metrics_names[0], scores[0]))
print('---------------------------------------------------')

pred = model.predict([[-0.294, 0.487, 0.180, -0.292, 0., 0.00149, -0.5311, -0.0333]])
print('예측 결과 : ', pred, ' ', np.where(pred > 0.5, 1, 0))
print('---------------------------------------------------')

#위의 내용을 다항분류로 처리
from keras.utils import to_categorical

#label은 one-hot처리
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print('y_train : ', y_train[0])

model = Sequential()
model.add(Dense(64, input_dim = 8, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(2, activation = 'softmax')) #확률값으로 나가야 하기 때문에 softmax

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['acc'])
model.fit(x_train, y_train, epochs = 100, batch_size = 32, verbose = 0, validation_split=0.2)
scores = model.evaluate(x_test, y_test)
print('이항분류 모델 성능 : %s : %.2f%%'%(model.metrics_names[1], scores[1] * 100)) #model.metrics_names[0]은 loss
print('이항분류 모델 성능 : %s : %.2f'%(model.metrics_names[0], scores[0]))
print('---------------------------------------------------')

pred = model.predict([[-0.294, 0.487, 0.180, -0.292, 0., 0.00149, -0.5311, -0.0333]])
print('예측 결과 : ', pred, ' ', np.argmax(pred))
print('---------------------------------------------------')


#label을 one-hot처리 마지막 출력 2개, softmax로 loss = 'categorical_crossentropy'  np.argmax 로 예측결과 출력



