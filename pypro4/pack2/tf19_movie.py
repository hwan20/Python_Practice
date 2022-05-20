#영화 리뷰 데이터(imdb dataset)로 이진 분류

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = 10000) #가장 자주 쓰이는 단어 10000가지만 보기 위하여
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape) #(25000,) (25000,) (25000,) (25000,)
print('훈련용 리뷰 개수 : {}'.format(len(x_train)))
print('테스트용 리뷰 개수 : {}'.format(len(x_test)))
num_classes = len(set(y_train))
print('카테고리 : {}'.format(num_classes))
print(set(y_train)) #{0, 1}

#라벨링된 실제 영문자료 확인
word_ind = imdb.get_word_index() #라벨링 데이터와 실제 데이터가 매핑되어 있음. dict타입으로 되어있다
#ex) {1:'good', 2:'hi'.......}
print(word_ind) #{'fawn': 34701, 'tsukino': 52006, ....
#print(word_ind.items()) #dict_items([('fawn', 34701), ('tsukino', 52006), ....

#key, value 타입으로 적혀있는 데이터를 value, key로 바꿈
reverse_word_index = dict([(value, key) for (key, value) in word_ind.items()]) #dict타입의 데이터 전체를 가져올 떄 items를 사용
print(reverse_word_index) #{34701: 'fawn', 52006: 'tsukino', ...
print(reverse_word_index.get(x_train[0][2])) #you

decode_review = ' '.join([reverse_word_index.get(i) for i in x_train[24999]]) #x_train데이터의 0번째부터 24999번째까지 포문을 돌면서 라벨링된 실제 데이터를 꺼냄
print(decode_review)
print('---------------------------------------------------')

#데이터 준비 : 입력데이터 feature에 대해서 one-hot encoding을 진행 - 25000개의 데이터 중에 데이터가 있는 부분만 1로 채우고 나머지는 0으로 채움 - 성능이 좋아짐
print(x_train[:1])

def vector_seq(sequences, dim = 10000):
    results = np.zeros((len(sequences), dim)) #시퀀스행 10000열짜리
    for i, seq in enumerate(sequences): #집합 데이터에 대해서 enumerate하면 index값이 따라옴
        results[i, seq] = 1.
    
    return results

x_train = vector_seq(x_train)
print(x_train[:1], x_train.shape) #[[0. 1. 1. ... 0. 0. 0.]] (25000, 10000)
x_test = vector_seq(x_test) #feature

y_train = np.asarray(y_train).astype('float32') #label을 float32타입으로 바꿈
y_test = np.asarray(y_test, 'float32') #이렇게 작서앻도 상관 X
print(y_train)
print('---------------------------------------------------')

#데이터 가공 끝 / model을 만듦
from keras import models, layers, regularizers
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10000,),
                kernel_regularizer = regularizers.l2(0.0001))) #regularizers.l2(0.0001)
model.add(Dense(32, activation='relu'))
model.add(Dropout(rate=0.3)) #모든 노드가 연산을 시작하니 과적합이 발생 rate=0.3은  30%는 연산에 참여하지 않음 - 과적합 방지
model.add(Dense(16, activation='relu'))
model.add(Dropout(rate=0.3))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
print(model.summary())

#훈련시 검증 데이터(validation data) 사용
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
print(len(x_val), len(partial_x_train)) #10000 15000

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train, partial_y_train, epochs = 30,
                    batch_size = 512, validation_data=(x_val, y_val), verbose = 2) #이미 split되어있는 데이터가 있으므로 validation_data를 준다
#validation_data, validation_split, k-fold 공통점 과적합 방지

print('모델 성능 평가 : ', model.evaluate(x = x_test, y = y_test))

#시각화
history_dict = history.history #
print(history_dict.keys())
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label = 'train loss')
plt.plot(epochs, loss, 'r-', label = 'validation loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()


acc = history_dict['acc']
val_acc = history_dict['val_acc']

plt.plot(epochs, acc, 'bo', label = 'train acc')
plt.plot(epochs, val_acc, 'r-', label = 'validation acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend()
plt.show()

pred = model.predict(x_test[:5])
print('실제값 : ', y_test[:5])
print('예측값 : ', np.where(pred > 0.5, 1, 0).flatten())


#과적합 방지
#1) train/test split, train-validation/test split, k-fold
#2) 가중치 규제(regularization)이다.
    #가중치 규제란 말 그대로 가중치의 값이 커지지 않도록 제한하는 기법이다.
    #가중치를 규제하면 모델의 일반화 성능이 올라간다.
    #regularizers를 이용해서 L1, L2 규제
    #L1규제 : L1규제는 손실 함수에 가중치의 절대값인 L1노름(norm)을 추가한다
    #L2규제 : L2규제는 손실 함수에 가중치에 대한 L2노름의 제곱을 더한다
#3) Dropout : 훈련하는 동안 층의 일부 노드를 훈련해서 제외
#4) Batch Normalization
#5) train data를 늘림
#기타 ....























