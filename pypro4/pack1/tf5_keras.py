#Keras : 텐서플로 기반의 DeepLearning 라이브러리(모듈)
#일관성있는 API를 지원
#ML(인공신경망) 모델을 매우 쉽게 작성할 수 있다


#환경변수 지정 -> 신경망 실행 -> 결과, 예측값과 실제값 비교 정확도 나옴 -> 정확도 만족하면 모델 저장,  아니면 신경망 재실행 
#신경망에서 결과 1회 실행하는 것을 epoch, 만족하지 못해 신경망 재실행하는 것을 역전파. 이때 w(가중치) 재설정

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

#OR 게이트 논리 모델을 생성 후 처리
#1. 데이터 셋 생성
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) #2차원 matrix
y = np.array([0, 1, 1, 1]) #1차원 vector

print(x) #feature
print(y) #label(class)

#2. 모델 구성
#model = Sequential([
#    Dense(input_dim = 2, units = 1), #입력은 2개, 출력은 1개
#    Activation('sigmoid') #2항 분류인 sigmoid를 사용 출력은 0또는 1
#])

#이렇게 쓰기도 함
model = Sequential()
model.add(Dense(units = 1, input_dim = 2)) 
model.add(Activation('sigmoid'))
#입력시 wx + b 가 입력됨 추세선을 그려야 하니 w가 있어야 하고 b가 없으면 0만 출력

#3. 모델 학습과정 설정(컴파일)
#model.compile(optimizer = 'sgd', loss = 'binary_crossentropy', metrics = ['accuracy']) #잘 안 씀
#model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])
#model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']) #sgd와 rmsprop의 단점을 보완함
#model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 0.1, momentum = 0.9),
#              loss = 'binary_crossentropy', metrics = ['accuracy']) 
#model.compile(optimizer = tf.keras.optimizers.RMSProp(learning_rate = 0.1),
#              loss = 'binary_crossentropy', metrics = ['accuracy']) 
#model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.1), #Adam이 제일 많이 쓰임
#              loss = 'binary_crossentropy', metrics = ['accuracy']) 
#RMSProp은 momentum이 자동으로 되어있다 
#momentum은 local과 global 미니멈이 있을 시에 local을 띄어넘음 
#learning_rate를 어떻게 주냐에 따라 loss의 변동 속도에 영향을 줄 수가 있다. 0.5면 학습률을 0.5씩 간다
#tf.keras.optimizer.SGD() 클래스를 직접 사용할 수가 있다 이렇게 사용하면 학습률을 설정할 수가 있음
#optimizer - cost를 작게 만들기 위해 쓰임 sgd - 경사하강법   즉 cost 작게 만들기 위해 경사하강법을 사용하겠다
#optimizer = rmsprop 확률적 경사하강법
#loss는 분류하기 위한 방법. sigmoid는 2진이니 binary가 앞에 붙음 분류니까 crossentropy 불순물이 없을 때까지 최대한 나눔
#분류니까 정확도가 필요하니 accuracy가 필요

#4모델 학습시키기
#model.fit(x, y, epochs = 10000, batch_size = 1, verbose = 2)

#5. 모델 평가
#loss_metrics = model.evaluate(x, y)
#print('loss_metrics : ', loss_metrics)

#6. 모델 사용해 예측하기
#pred = model.predict(x)
#print('예측결과 : ', pred)
#print('예측결과 : ', (pred > 0.5).astype('int32'))
#print('예측결과 : ', (model.predict(x) > 0.5).astype('int32'))


#모델 성능이 우수하다고 판단되면 모델을 저장
model.save('test.hdf5') #hdf5확장명은 대용량 데이터의 파일을 저장하기 위한 확장자이다
#모델을 저장하면 위의 과정은 필요가 없다

#del model

#저장된 모델 읽기
from keras.models import load_model
model2 = load_model('test.hdf5')
print('예측결과 : ', (model2.predict(x) > 0.5).astype('int32'))


