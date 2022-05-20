#wine dataset을 이용하여 레드와 화이트 와인 분류 (이항 분류)
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

wdf = pd.read_csv('../testdata/wine.csv', header = None)
print(wdf.head())
print(wdf.info()) #결측치와 데이터 타입을 바꿀 필요가 없다
print(wdf.iloc[:, 12].unique()) #12열의 데이터 값을 확인 [1 0]  2진 분류할 것
print(len(wdf[wdf.iloc[:, 12] == 0])) #12열의 데이터가 0인 데이터의 갯수 확인  4898
print(len(wdf[wdf.iloc[:, 12] == 1])) #12열의 데이터가 1인 데이터의 갯수 확인  1599
print('---------------------------------------------------')

#12열이 label 나머지가 feature
dataset = wdf.values
x = dataset[:, 0:12] #0번째 열부터 11번째 열까지의 데이터를 x에 넣음
y = dataset[:, -1] #마지막 열인 12번째 열의 데이터를 y에 넣음
print(x[:1])
print(y[:1])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12) #shuffle은 기본값

#데이터를 나눴으니 학습을 시킴
model = Sequential()
#model.add(Flatten()) #Flatten() 차원을 축소해주는 클래스. keras.layers가 지원해줌. 완전 연결층에 들어갈 때 1차원으로 들어가야 되니 차원을 축소해줌
#내부적으로 차원을 축소시켜 쓰지 않아도 상관은 없다.  원래는 사용해서 데이터를 일렬로 입력시켜줘야 함
model.add(Dense(32, input_dim = 12, activation = 'relu')) #12개의 데이터가 들어와서 32개의 노드로 빠져나감
model.add(Dense(16, activation = 'relu')) #relu가 안 되면 위키relu? 엘루? 등 다양한 모델을 사용
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid')) #2항으로 나눌거니 sigmoid

model.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])
print(model.summary())

#fit() 전에 모델 정확도를 확인
loss, acc = model.evaluate(x_train, y_train)
print('훈련 전 모델의 성능 : {:5.2f}%'.format(acc * 100)) #정확도를 5개를 100분율 소수 2번쨰 까지 확인
print('---------------------------------------------------')

early_stop = EarlyStopping(monitor = 'loss', patience = 5) #loss가 줄다가 5번 동안 더 이상 줄지 않으면 멈춘다

#학습 중 model 저장
#저장 폴더를 따로 만들어서 사용 가능
import os
MODEL_DIR = "./wine_model/"#데이터가 변하지 않는 상수일 때 대문자를 사용(java에서는 final 함수 사용)
if not os.path.exists(MODEL_DIR): #경로에 MODEL_DIR 폴더가 있지 않다면
    os.mkdir(MODEL_DIR)

#modelPath = MODEL_DIR + "{epoch:02}_{loss:.3f}.hdf5"
#제일 마지막 파일이 성능이 제일 좋은 모델이라 마지막 파일만 저장
modelPath = MODEL_DIR + "wine_model.hdf5" #가장 마지막 파일(제일 좋은 성능의 모델)만 저장
chkPoint = ModelCheckpoint(filepath = modelPath, monitor = 'loss', save_best_only=True)
#loss를 모니터링하여 모델이 좋아질 때만 파일로 저장


#history를 사용해서 시각화가 가능 history가 나오면 시각화를 한다고 생각하면 됨
history = model.fit(x_train, y_train, epochs = 1000, batch_size = 64,
                    validation_split = 0.2, #데이터를 20%만큼 학습시에 비교함... 오버피팅이 의심스러우니 사용
                    callbacks = [early_stop, chkPoint], verbose = 2) #batch_size 기본 값은 30.  30번째 마다 label과 비교
#early_stop, chkPoint 둘 다 최적의 성능이 나올 때 실행한다는 점에서 비슷함
#validation_split를 사용했다면 monitor = 'val_loss'를 사용할 수가 있다

#fit() 훈련 후 모델 정확도 확인
loss, acc = model.evaluate(x_test, y_test)
print('훈련 전 모델의 성능 : {:5.2f}%'.format(acc * 100))
#61번 학습을 한 후에 멈춤. 98.15%

#모델의 성능이 만족스러우니 모델을 저장하여 사용
#model.save()
#내가 직접 성능이 좋은 모델을 판단해 저장 한다면 model.save("파일명.확장자명") - ModelCheckpoint를 사용하면 가장 좋은 모델을 알아서 저장이 가능

#history관련
vloss = history.history['val_loss']
print('vloss : ', vloss, len(vloss))
vacc = history.history['val_accuracy'] #metrics=['accuracy']에 작성한 이름과 맞아야 한다
print('vacc : ', vacc, len(vacc))
loss = history.history['loss']
print('loss : ', loss, len(loss))
acc = history.history['accuracy'] #metrics=['accuracy']에 작성한 이름과 맞아야 한다
print('acc : ', acc, len(acc))

#시각화
epoch_len = np.arange(len(acc)) #0~len까지의 수열이 만들어짐
plt.plot(epoch_len, vloss, c='red', label = 'val_loss')
plt.plot(epoch_len, loss, c='blue', label = 'loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(loc = 'best')
plt.show()


plt.plot(epoch_len, vacc, c='red', label = 'val_acc')
plt.plot(epoch_len, acc, c='blue', label = 'acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend(loc = 'best')
plt.show()

#예측
#베스트 모델이 저장되었으므로, 더 이상의 학습은 진행하지 않는다
#베스트 모델을 읽어서 새로운 데이터에 대한 분류 작업을 진행

from keras.models import load_model
mymodel = load_model('wine_model/wine_model.hdf5')
new_data = x_test[:5, :] #새로운 데이터를 넣는다고 가정하고 진행
print(new_data)
pred = mymodel.predict(new_data)
print('분류 결과 : ', np.where(pred > 0.5, 1, 0).flatten())













