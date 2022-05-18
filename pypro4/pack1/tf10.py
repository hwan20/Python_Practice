#단순 성형회귀모델 작성 방법 세가지 경험하기
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np

#공부 시간에 따른 성적 데이터
x_data = np.array([1, 2, 3, 4, 5], dtype = np.float32)
y_data = np.array([11, 32, 53, 64, 70], dtype = np.float32)
print(np.corrcoef(x_data, y_data)) #0.9743547
print('-------------------------------------')

#모델 작성 방법1 : Sequential api : 가장 일반적이고 단순한 방법
model = Sequential()
model.add(Dense(units = 2, input_dim = 1, activation = 'linear'))
model.add(Dense(units = 1, activation = 'linear')) #linear 안 써도 됨
print(model.summary())
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model.compile(optimizer = opti, loss = 'mse', metrics = ['mse'])
history = model.fit(x = x_data, y = y_data, batch_size = 1, epochs = 100, verbose = 0)
loss_metrics = model.evaluate(x = x_data, y = y_data)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data))) #이건 tensorflow에 없다
print('실제값 : ', y_data)
print('예측값 : ', model.predict(x_data).flatten())

new_data = [1.5, 2.3, 5.8]
print('새 예측값 : ', model.predict(new_data).flatten())

#시각화
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
#plt.show()

#보고서에는 loss가 떨어지는 것도 시각화 해서 보여줘야 함
#plt.plot(history.history['loss'], label = '손실')
#plt.xlabel('학습횟수')
plt.plot(history.history['mse'], label = '평균제곱오차') #loss대신 mse로 봐도 된다
plt.xlabel('학습횟수')
plt.legend()
#plt.show()



#모델 작성 방법2 : function api : 유연한 구조. 입력 데이터로 여러 층을 공유하거나 다양한 종류의 입출력 사용이 가능
#*1번 방법보다 더 중요 책에서 보기 힘듬

from keras.layers import Input
from keras.models import Model

#각 층은 일종의 함수처럼 처리함
inputs = Input(shape = (1,)) #shape는 tuple형식으로
outputs1 = Dense(2, activation = 'linear')(inputs)
outputs = Dense(1, activation = 'linear')(outputs1)

model2 = Model(inputs, outputs)

#아래는 방법 1과 동일
print(model2.summary())
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model2.compile(optimizer = opti, loss = 'mse', metrics = ['mse'])
history = model2.fit(x = x_data, y = y_data, batch_size = 1, epochs = 100, verbose = 0)
loss_metrics = model2.evaluate(x = x_data, y = y_data)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model2.predict(x_data))) #이건 tensorflow에 없다
print('실제값 : ', y_data)
print('예측값 : ', model2.predict(x_data).flatten())



#모델 작성 방법3 : sub classing : 동적인 구조의 네트워크를 형성. 고난이도의 작업에서 활용성이 높음
x_data = np.array([[1], [2], [3], [4], [5]], dtype = np.float32)
y_data = np.array([11, 32, 53, 64, 70], dtype = np.float32)

#from keras.models import Model #모델을 상속을 받음
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(2, activation = 'linear')
        self.d2 = Dense(1, activation = 'linear')

    def call(self, x):
        inputs = self.d1(x)
        return self.d2(inputs)

model3 = MyModel()

#아래는 방법 1과 동일
#print(model3.summary())
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model3.compile(optimizer = opti, loss = 'mse', metrics = ['mse'])
history = model3.fit(x = x_data, y = y_data, batch_size = 1, epochs = 100, verbose = 0)
loss_metrics = model3.evaluate(x = x_data, y = y_data)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model3.predict(x_data))) #이건 tensorflow에 없다
#print('실제값 : ', y_data)
#print('예측값 : ', model3.predict(x_data).flatten())
#방법 1부터 3은 모델의 설계도 작성 방법만 다르다



#모델 작성 방법3-1 : custom layer + sub classing : 동적인 구조의 네트워크를 형성. 고난이도의 작업에서 활용성이 높음
from keras.layers import Layer
#상속받는 방법이 다름. Layer를 상속받음
#custom layer : 사용자 정의층 사용
class Linear(Layer):
    def __init__(self, units = 1):
        super(Linear, self).__init__()
        self.units = units
    
    def build(self, input_shape): #call호출, 가중치 관련 내용을 적을 수 있다
        self.w = self.add_weight(shape = (input_shape[-1], self.units),
                                 initializer = 'random_normal', trainable = True)
        self.b = self.add_weight(shape = (self.units,), #b값은 w값의 출력 계수와 맞춰줌 tuple형식
                                 initializer = 'zeros', trainable = True) 
    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b #y = wx + b 의 식을 return해줌
#initializer = 'random_normal' 처음 w값은 랜덤 값으로 줌
#trainable = True 역전파를 진행 안 주면 반복 학습 진해을 안 해서 성능이 확 떨어짐


class MLP(Model):

    def __init__(self):
        super(MLP, self).__init__()
        #self.linear1 = Linear(1) #class Linear(Layer): 이걸 부르는것
        self.linear1 = Linear(2)
        self.linear2 = Linear(1)

    def call(self, inputs): 
        #return self.linear1(inputs)
        x = self.linear1(inputs)
        return self.linear2(x)

model4 = MLP()

#아래는 방법 1과 동일
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model4.compile(optimizer = opti, loss = 'mse', metrics = ['mse'])
history = model4.fit(x = x_data, y = y_data, batch_size = 1, epochs = 100, verbose = 0)
loss_metrics = model4.evaluate(x = x_data, y = y_data)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model4.predict(x_data))) #이건 tensorflow에 없다
#print('실제값 : ', y_data)
#print('예측값 : ', model4.predict(x_data).flatten())

tf.keras.utils.plot_model(model, 'abc.png')





