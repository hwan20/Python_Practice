#다항분류 : 최종 출력값이 softmax함수를 통해 확률값으로 여러 개가 출력(출력 결과가 3개 이상)
#이 중에서 확률값이 가장 큰 인덱스를 분류의 결과로 얻음
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical  #one-hot encoding을 지원
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

np.random.seed(1)
#tf.random.set_seed(1) #위와 같음

xdata = np.random.random((1000, 12)) #시험 점수라고 가정 1000행 12열
ydata = np.random.randint(5, size = (1000, 1)) #범주 5개, 시험 과목 - 0:국어 ~ 4:체육이라고 가정
print(xdata[:2])
print(ydata[:2]) #[[2][0]] 학습시 label은 one-hit 처리 후 학습에 참여
#다항 분류일 경우에는 label을 split으로 나눈 후 대표값으로 설정한다

ydata = to_categorical(ydata, num_classes = 5)
print(ydata[:2])
#[[0. 0. 1. 0. 0.]
# [1. 0. 0. 0. 0.]]

#print(np.argmax(i) for i in ydata[:2]) #객체 값으로 나오니 list로 변환하여 출력해야 함
print([np.argmax(i) for i in ydata[:2]]) #아규먼트의 가장 큰 값을 반환
print('---------------------------------------------------')

#모델 작성
model = Sequential()
model.add(Dense(units = 32, input_shape = (12, ), activation = 'relu')) #입력은 12개
model.add(Dense(units = 16,activation = 'relu'))
model.add(Dense(units = 5,activation = 'softmax')) #soft max로 빠져나가는 값이 5개로 나감

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
#loss = 'categorical_crossentropy' 범주형일(다항분류) 경우 사용

print(model.summary())

history = model.fit(xdata, ydata, epochs = 2000, batch_size = 32, verbose = 2, shuffle = True) #shuffle은 batch와 관련되어 있다. 훈련할 때마다 중복 없이 추출 비복원 추출.
model_eval = model.evaluate(xdata, ydata)

print('model_eval : ', model_eval) #loss와 acc가 나옴
print('---------------------------------------------------')

#시각화
plt.plot(history.history['loss'], label = 'loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label = 'accuracy')
plt.xlabel('epochs')
plt.legend()
plt.show()

#예측 - 랜덤값이라 완전하지는 않지만 순서 중요
print('예측값 : ', model.predict(xdata[:5])) #이렇게 하면 확률값으로 나옴
print('예측값 : ', [np.argmax(i) for i in model.predict(xdata[:5])])
print('실제값 : ', ydata[:5])
print('실제값 : ', [np.argmax(i) for i in ydata[:5]])
print('---------------------------------------------------')

#새로운 값으로 예측
x_new = np.random.random([1, 12])
print(x_new)
new_pred = model.predict(x_new)
print('분류 결과 : ', new_pred)
print('분류 결과 : ', np.argmax(new_pred)) #입력값이 하나라 반복문 돌리면서 빼지 않아도 됨
print('분류 결과 합 : ', np.sum(new_pred))
print('---------------------------------------------------')

#과목명으로 나오기 원하면
CLASSES = np.array(['국어', '영어', '수학', '과학', '체육'])
print('분류 결과 : ', CLASSES[np.argmax(new_pred)])

