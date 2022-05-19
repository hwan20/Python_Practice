#자동차 관련 데이터로 선형회귀모델 작성
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snf
import tensorflow as tf
from keras import layers
from pip._internal import network

dataset = pd.read_csv('../testdata/auto-mpg.csv')
print(dataset.head(2))
del dataset['car name']
print(dataset.columns)
print(dataset.corr())
dataset.drop(['acceleration', 'model year', 'origin'], axis = 'columns', inplace = True)
print(dataset.info())

#obj타입인 horsepower의 데이터 타입을 numeric으로 바꿈 
dataset['horsepower'] = dataset['horsepower'].apply(pd.to_numeric, errors='coerce')
#print(dataset.info())
print(dataset.isna().sum()) #horsepower에 결측치가 6개 있음
#horsepower의 데이터의 갯수가 부족함. 결측치가 있음 horsepower에 맞춰 나머지 버림
dataset = dataset.dropna()
print(dataset.info())

print(dataset.head(2))

#sns.pairplot(dataset[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight']])
#plt.show()

#train/test split : sample() 함수
train_data = dataset.sample(frac = 0.7, random_state = 123)
test_data = dataset.drop(train_data.index)
print(train_data[:2], ' ', train_data.shape) #(274, 5)
print(test_data[:2], ' ', test_data.shape) #(118, 5)
print('-----------------------------------')

#train data에 대한 표준화 선행 작업
train_stat = train_data.describe()
train_stat.pop('mpg') #python에 있는 명령어로 mpg칼럼이 빠짐
train_stat = train_stat.transpose() #행과 열의 위치를 바꿔줌
print(train_stat) #mean과 std 등의 값을 알기 위해 작성해놓음
print('-----------------------------------')

#label : mpg(연비)
train_label = train_data.pop('mpg')
test_label = test_data.pop('mpg')
print(train_label[:2])
print(test_label[:2])
print('-----------------------------------')

#feature에 대해 표준화 진행
#print(train_data[:2])
def st_func(x): #(요소값 - 평균) / 표준편차
    return(x - train_stat['mean']) / train_stat['std']

#print(st_func(10))
#print('-----------------------------------')
#print(st_func(train_data[:2]))
#print('-----------------------------------')

st_train_data = st_func(train_data)
st_test_data = st_func(test_data)

print(st_train_data[:3])
print(train_label[:3])
print('-----------------------------------')
#     cylinders  displacement  horsepower    weight
#222   1.450601      0.599039    0.133053  1.247890
#247  -0.873754     -1.042328   -0.881744 -1.055604
#136   1.450601      0.992967    0.894151  1.341651
#        mpg
#222    17.0
#247    39.4
#136    16.0
#cylinders  displacement  horsepower    weight 칼럼과 mpg칼럼은 반비례 관계이다


from keras.models import Sequential
from keras.layers import Dense

def build_model():
    network = Sequential([
        Dense(units=64, activation = tf.nn.relu, input_shape = [4,]),
        Dense(units=64, activation = tf.nn.relu),
        Dense(units=1, activation = 'linear'),
    ])
    
    #opti = tf.keras.optimizers.RMSprop(0.001)
    opti = tf.keras.optimizers.Adam(0.01)
    network.compile(optimizer=opti, loss='mean_squared_error',
                    metrics=['mean_absolute_error', 'mean_squared_error']) #mae, mse
    return network
model = build_model()
print(model.summary())
print('-----------------------------------')

#fit 전에 predict() 가능은 하지만 성능은 기대하지 말자
epochs = 5000 #조기종료할 것이므로 일단 많이 준다
early_stop = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', mode = 'auto', patience = 5)

history = model.fit(st_train_data, train_label, batch_size = 32, epochs = epochs,
                    validation_split = 0.2, verbose = 1, callbacks=[early_stop])
df = pd.DataFrame(history.history)
print(df.columns)
print(df.head())
print('-----------------------------------')


#모델 성능(mae, mse) 확인 시각화
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure(figsize = (8, 12))
    
    #1행
    plt.subplot(2, 1, 1)
    plt.xlabel('epochs')
    plt.ylabel('mae[MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label = 'train err')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label = 'val err')
    plt.legend()
    
    #2행
    plt.subplot(2, 1, 2)
    plt.xlabel('epochs')
    plt.ylabel('mse[$MPG^2$]') #제곱의 형태를 띄기 위해서 ^2$ 사용
    plt.plot(hist['epoch'], hist['mean_squared_error'], label = 'train err')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label = 'val err')
    plt.legend()
    plt.show()
    
plot_history(history)
