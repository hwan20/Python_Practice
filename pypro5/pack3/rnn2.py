#문자열 토큰 처리 + LSTM으로 감성 분석

from keras.preprocessing.text import Tokenizer

samples = ['The cat say on the mat.', 'The dog ate my homework.']

#토큰 분리 방법 1
token_index = {}

for sam in samples:
    for word in sam.split(sep=' '): #영문이니 띄어쓰기를 기준으로 단어 나누기
        if word not in token_index:
            #print(word) #대소문자나 . 그대로 살아있음
            token_index[word] = len(token_index)
print(token_index) #단어와 인덱스 순으로 저장함


#토큰 분리 방법2 - Tokenizer
tokenizer = Tokenizer(num_words = 15) #벡터의 크기를 지정할 수 있다
tokenizer.fit_on_texts(samples) #list타입이어야됨  token처리됨
token_seq = tokenizer.texts_to_sequences(samples)
#['The cat say on the mat.', 'The dog ate my homework.']
#텍스트를 정수 인덱스로 만들어서 리스트 타입으로 반환하고 있다
print(token_seq) #[[1, 2, 3, 4, 1, 5], [1, 6, 7, 8, 9]]
print(tokenizer.word_index) #토큰처리된 단어들은 대문자->소문자로 바뀌게 되고 .이 사라짐  '은 그대로 사용됨
print('---------------------------------------------')


#토큰으로 매트릭스를 만듦
token_met = tokenizer.texts_to_matrix(samples, mode='binary') 
#mode='count' 단어 등장 횟수 'tfidf'는 가중치 'freq'는 확률 'binary'는 원핫 처리 단어의 존재 여부만 확인
#binary의 첫 번째는 어떤 단어도 포함되지 않는 인덱스가 있어 0이 나옴 - 무시하고 봐야함
print(token_met)

print(tokenizer.word_counts) #단어의 순서대로 등장 횟수를 튜플 형식으로 보여줌
print(tokenizer.document_count) #문장 갯수를 보여줌 2개의 문장
print(tokenizer.word_docs) #어느 문장에서 나오는지를 보여줌
print('---------------------------------------------')


from keras.utils import to_categorical
print(to_categorical(token_seq[0], num_classes=6)) #
print('---------------------------------------------')

#감성 처리법
docs = ['너무 재밌어요', '최고예요', '참 잘 만든 작품이에요', '추천하고 싶어요', '한번 더 보고 싶어요',
        '글쎄요', '별로인데요', '생각보다 만족스럽지 않네요', '마음에 들지 않아요', '재미없어요']

import numpy as np
labels = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) #1:긍정, 0:부정

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)

x = token.texts_to_sequences(docs)
print('토큰화 결과 : ', x) 
print('---------------------------------------------')

#토큰의 크기가 다름. 다르면 처리하기 힘드니 토큰의 크기를 맞춰주기 - 패딩이라고 함
#토큰의 인덱싱 벡터의 크기를 일정하게 만들기
from keras.utils import pad_sequences
padding_x = pad_sequences(x, 4) #제일 큰 인덱스의 크기가 4이니 4에 맞춰서 크기를 맞춰줌
print('패딩 결과 : ', padding_x)

word_size = len(token.word_index) + 1 #임베딩에 입력될 단어의 수. 가능한 토큰의 수는 단어 인덱스 최대값 +1을 준다
print('word_size : ', word_size) #21

#model 작성
from keras.models import Sequential
from keras.layers import SimpleRNN,LSTM,GRU,Dense, Embedding, Flatten

model = Sequential()
model.add(Embedding(word_size, 8, input_length=4)) #word_size입력될 총 단어 수 , input_length=4는 계산하는 시퀀스를 4개 사용
model.add(LSTM(32)) #activation='tanh' 생략하면 tanh -> 활성화 함수
model.add(Flatten()) #FClayer
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())

#문자열을 그대로 전달하는 게 아니고 토큰화 하여 전달 - 크기가 일정하지 않으니 크기를 맞춰주기 위해 패딩을 진행
#즉 패딩된 토큰을 전달

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padding_x, labels, epochs=20, verbose=2)
print('acc score : %.4f'%(model.evaluate(padding_x, labels)[1]))

print('예측값 : ', np.where(model.predict(padding_x) > 0.5, 1, 0).ravel())
print('실제값 : ', labels)

