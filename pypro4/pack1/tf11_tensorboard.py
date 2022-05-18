#TensorBoard : 모델의 구조 및 학습 과정/결과 등을 시각화하여 볼 수가 있다
#matplotlib 라이브러리를 이용하는 것이 아닌 별도의 웹 서버를 구동하여 볼수 있음
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.callbacks import TensorBoard

#다중선형 모델 : 5명이 세 번의 시험 점수로 다음 번 시험 점수를 예측 (연속형 데이터)
x_data = np.array([[70, 85, 80], [71, 88, 78], [50, 80, 60], [66, 20, 60], [50, 30, 10]])
y_data = np.array([73, 82, 72, 57, 34])

model = Sequential()
model.add(Dense(6, input_dim = 3, activation = 'linear', name = 'a')) #3개가 들어와서 6개로 빠져나감
model.add(Dense(3, activation = 'linear', name = 'b'))
model.add(Dense(1, activation = 'linear', name = 'c'))

opti = tf.keras.optimizers.Adam(learning_rate = 0.01)
model.compile(optimizer = opti, loss = 'mse', metrics = ['mse'])
print(model.summary())

#텐서보드 설정
tb = TensorBoard(log_dir = '.\\my', histogram_freq = True, write_graph = True, write_images = True)
history = model.fit(x_data, y_data, batch_size = 1, epochs = 30, verbose = 2,
                    callbacks=[tb])
#실행을 한 후에 module이 있는 하위 폴더에 파일이 있는지 확인한다
#anaconda 프롬프트를 실행한 후
#cd C:\work\repo\pypro4\pack1
#tensorboard --logdir my/
#입력하면 나오는 localhost를 주소창에 입력하면 된다


#import matplotlib.pyplot as plt
#plt.plot(history.history['loss'])
#plt.ylabel('loss')
#plt.xlabel('epochs')
#plt.show()

loss_metrics = model.evaluate(x_data, y_data)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('결정계수 : ', r2_score(y_data, model.predict(x_data)))







