#보스톤 집값 데이터로 분류 모델
import numpy as np
from keras import models, layers
from keras.datasets import boston_housing

aa = boston_housing.load_data()
#print(aa, type(aa))
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()
#튜플 형식으로 잘라서 가져옴 기본 값인 8:2 비율로 저장
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape) #(404, 13) (404,) (102, 13) (102,)

print(x_train[:2]) #13개의 행으로 하나의 집값을 결정하는 중
#print(x_test[:2])
print(y_train[:2])

#상관관계를 확인하여 볼 수도 있지만 np.array()로 바꿔야됨

#feature의 데이터가 다를 떄 표준화와 정규화가 모델의 성능에 도움을 많이 주니 해야하는 게 좋음
#feature에 대한 스케일링 : 표준화, 정규화
#모델을 사용해 표준화
#from sklearn.preprocessing import StandardScaler
#x_train = StandardScaler().fit_transform(x_train)
#print(x_train[:1])
#[[-0.27224633 -0.48361547 -0.43576161 -0.25683275 -0.1652266  -0.1764426
#   0.81306188  0.1166983  -0.62624905 -0.59517003  1.14850044  0.44807713
#   0.8252202 ]]


#직접 수식을 사용해 표준화 : (요소값 - 평균) / 표준편차
mean = x_train.mean(axis = 0) #평균
x_train -= mean #요소값 - 평균
std = x_train.std(axis = 0) #표준편차
x_train /= std
print(x_train[:1])
#[[-0.27224633 -0.48361547 -0.43576161 -0.25683275 -0.1652266  -0.1764426
#   0.81306188  0.1166983  -0.62624905 -0.59517003  1.14850044  0.44807713
#   0.8252202 ]]

x_test -= mean
x_test /= std
#print(x_test[:1])


#표준화를 하고 함수에 담아둘 수가 있따
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation = 'linear', input_shape = (x_train.shape[1],))) 
    #input_dim을 input_shape으로 줘도 된다 그대신 tuple형식으로 줘야됨
    #x_train.shape[1] 은 (404, 13)의 1번째 즉 13개를 준다는 뜻
    model.add(layers.Dense(32, activation = 'linear')) #activation = 'relu' 보통은 relu를 많이 씀
    model.add(layers.Dense(1, activation = 'linear')) #마지막 layer만 분류 형식에 맞춰서 써야된다
    model.compile(optimizer = 'adam', loss = 'mse', metrics = ['mse'])
    return model
'''
model = build_model()
print(model.summary())


#방법1 : train/test split
#history = model.fit(x_train, y_train, epochs = 50, batch_size = 10, verbose = 1)

#방법2 : train-validation/test split
history = model.fit(x_train, y_train, epochs = 50, batch_size = 10, 
                    validation_split = 0.2, verbose = 0) #validation_split = 0.2 훈련하는 동안 20%를 검증함

mse_history = history.history['mse'] #metrics = ['mse']에 따라 가야함
print('mse_history : ', mse_history)

val_history = history.history['val_mse'] #validation의 값을 확인할 수 있다
print('val_history : ', val_history)

#import matplotlib.pyplot as plt
#plt.plot(mse_history, 'r', label = 'mse or loss')
#plt.plot(val_history, 'b', label = 'val_mse or val_loss')
#plt.xlabel('epochs')
#plt.ylabel('mse')
#plt.legend()
#plt.show()
#시각화를 하여 학습률에 대해 보면서 학습률이 너무 많아 오히려 안 좋아지면 중간에 학습률을 끊은 후 모델을 저장할 수 있다

#predict
print('예측값 : ', np.squeeze(model.predict(x_test[:5])))
print('실제값 : ', y_test[:5])

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_test, model.predict(x_test))) #0.69842
print('-----------------------------------')
'''
#concatenate : numpy배열 결합
a = np.array([[1, 2], [3, 4]]) #2행 2열 매트릭스
b = np.array([[5, 6], [7, 8], [9, 10]]) #3행 2열 매트릭스
print(np.concatenate((a, b), axis = 0)) #열기준
print(np.concatenate((a, b.T), axis = 1)) #행기준
print(np.concatenate((a, b), axis = None)) #첫 번째 배열부터 가로방향 - 차원 축소
print('-----------------------------------')

#모델 학습 및 검정 : k-fold 적용 - 비교적 가용 데이터가 적은 경우에 효과적 
k = 4
val_samples = len(x_train) // k
all_mse_history = []

for i in range(k):
    #print('i : ', i)
    #train data의 일부를 validation data로 사용하기 위해 데이터 추출
    #전체 데이터 수 404개
    #print(i * val_samples, ':', (i + 1) * val_samples) #0 : 101, 101: 202, 202 : 303, 303 : 404
    val_x = x_train[i * val_samples:(i + 1) * val_samples] #validation data
    val_y = y_train[i * val_samples:(i + 1) * val_samples]
    #print(val_x.shape, ' ', val_y.shape) #(101, 13)   (101,) 101개씩 학습을 시작하기 위해
    #print(val_x[:1])
    #101개씩 validation하여 train 한 후 학습 
    #validation data를 제외한 나머지는 train
    train_x = np.concatenate([x_train[:i * val_samples], x_train[(i + 1) * val_samples:]], axis=0)
    train_y = np.concatenate([y_train[:i * val_samples], y_train[(i + 1) * val_samples:]], axis=0)
    #print(train_x.shape, ' ', train_y.shape) #(303, 13)   (303,)

    model2 = build_model()
    history2 = model2.fit(train_x, train_y, epochs = 50, batch_size = 10,
                         validation_data = (val_x, val_y), verbose = 0)
    
    mse_history2 = history2.history['mse'] #metrics = ['mse']에 따라 가야함
    print('mse_history2 : ', mse_history2)
    
    val_history2 = history2.history['val_mse'] #validation의 값을 확인할 수 있다
    print('val_history2 : ', val_history2)
    all_mse_history.append(mse_history2)
print('-----------------------------------')
    
import matplotlib.pyplot as plt
plt.plot(mse_history2, 'r', label = 'mse or loss')
plt.plot(val_history2, 'b', label = 'val_mse or val_loss')
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()
#시각화를 하여 학습률에 대해 보면서 학습률이 너무 많아 오히려 안 좋아지면 중간에 학습률을 끊은 후 모델을 저장할 수 있다

print('k-fold 전체 평균 : ', np.mean(all_mse_history))
print('-----------------------------------')

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_test, model2.predict(x_test))) #0.743706

