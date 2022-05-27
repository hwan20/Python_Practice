#RNN을 이용한 텍스트 생성 : 문맥을 반영해서 다음 단어를 예측하고 텍스트를 생성하기

from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences, to_categorical
import numpy as np
from keras.layers import Embedding, Dense, LSTM, Flatten
from keras.models import Sequential

#text = """경마장에 있는 말이 뛰고 있다
#그의 말이 법이다
#가는 말이 고와야 오는 말이 곱다"""

text = """은행들의 점포 폐쇄는 지난 2015년 이후부터 매년 이어지고 있다.
특히 지난 2020년부터는 코로나19 확산으로 인해 속도가 더 빨라졌다.
은행들의 점포 폐쇄 이유는 비용절감 때문이다.
임대료 등의 유지비용은 해가 갈수록 계속 늘어나고 있다."""


#토큰화 하고 정수 인코딩
tok = Tokenizer()
tok.fit_on_texts([text]) #list 타입을 원함
encoded = tok.texts_to_sequences([text])[0] #메트릭스 형태의 값을 벡터로 뽑아냄
print(encoded) #text의 글이 인코딩된 인덱스 번호로 설정되어 있음
print(tok.word_index) #글에 해당하는 인덱스 번호를 보여줌

vocab_size = len(tok.word_index) + 1 #+1을 주는 이유는 keras의 index번호가 0으로 시작하니 단어 집합의 크기보다 1을 더 크게 만듦

#훈련 데이터 만들기
sequences = list()
for line in text.split('\n'): #문장 토큰화 \n을 기준으로 문장별로 자름 
    enco = tok.texts_to_sequences([line])[0] #\n을 기준으로 잘라진 한 라인씩 할 거니
    #print(enco) #text의 줄이 각 줄마다 인코딩됨
    
    #바로 다음 단어를 label로 사용하기 위해 리스트에 벡터 담기 
    for i in range(1, len(enco)):
        sequ = enco[:i + 1] #전 단어를 feature를 삼고 다음 단어를 label로 삼기 위해 +1을 씌어줌
        #print(sequ) #[2, 3]이 feature [2, 3, 1]의 1이 label
        sequences.append(sequ)
print('---------------------------------------------')

print('학습에 참여할 샘플 수 : %d'%len(sequences)) #11
print(sequences) #[2, 3], [2, 3, 1], [2, 3, 1, 4] 벡터 안의 마지막 숫자가 label
print('---------------------------------------------')

#2칸 짜리 벡터도 있고 5칸 짜리 벡터도 있으니 크기를 맞춰주기
print(max(len(i) for i in sequences)) #sequences안에 있는 모든 벡터 중에서 가장 길이가 긴 값 출력 

#전체 벡터 각각의 길이를 통일
max_len = max(len(i) for i in sequences)

psequences = pad_sequences(sequences, maxlen=max_len, padding='pre') 
#padding='pre' 기본이 pre, 빈 값을 왼쪽부터 채움 post면 오른 쪽으로 채움
print(psequences)
#[[ 0  0  0  0  2  3]
# [ 0  0  0  2  3  1]
print('---------------------------------------------')


#각 벡터의 마지막 요소(단어)를 레이블로 사용하기 위해 분리
x = psequences[:, :-1] #모든 행의 마지막 열 전까지 값을 가짐 - feature
y = psequences[:, -1] #label
print(x)
print(y)
print('---------------------------------------------')

#label을 onehot처리 -> sofrmax를 쓰니까
y = to_categorical(y, num_classes=vocab_size)
print(y[:2])
print('---------------------------------------------')

#model 작성
model = Sequential()
model.add(Embedding(vocab_size, 32, input_length=max_len-1)) 
#input_length하나를 빼줘야 함. 마지막 하나는 레이블로 빠졌으니
model.add(LSTM(32)) #activation='tanh' 생략하면 tanh -> 활성화 함수
model.add(Flatten()) 
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
print('---------------------------------------------')

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=200, verbose=2)
print('model.evaluate : ', model.evaluate(x, y))
print('---------------------------------------------')

#문자열을 생성 함수
def sequence_gen_text(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0] #현재 단어에 대한 정수 인코딩
        encoded = pad_sequences([encoded], maxlen=max_len-1, padding='pre')
        result = np.argmax(model.predict(encoded, verbose=0), axis=-1)
        
        #예측 단어 찾기
        for word, index in t.word_index.items():
            #print(word, index)
            if index == result: #해당 단어가 예측 단어이기 때문에 더 이상 돌릴 필요가 없다
                break
            
        current_word = current_word + ' ' + word
        sentence = sentence + ' ' + word
    
    sentence =  init_word + sentence
    return sentence
    
# print(sequence_gen_text(model, tok, '경마', 1))
# print(sequence_gen_text(model, tok, '그의', 1))
# print(sequence_gen_text(model, tok, '가는', 1))
# print(sequence_gen_text(model, tok, '경마장에', 4))

print(sequence_gen_text(model, tok, '은행들의', 3))
print(sequence_gen_text(model, tok, '특히', 4))
print(sequence_gen_text(model, tok, '점포', 2))
print(sequence_gen_text(model, tok, '갈수록', 1))

