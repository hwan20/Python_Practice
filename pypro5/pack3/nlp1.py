#자연어 처리
#Word embedding : 워드를 수치화해서 벡터화
#카테고리컬 인코딩 : 레이블 인코딩(문자를 숫자화), 원핫 인코딩(0과 1의 조합)

#레이블 인코딩
datas = ['python', 'lan', 'program', 'computer', 'say']
datas.sort()

print(datas)

values = []
for x in range(len(datas)):
    values.append(x)

print(values, ' ', type(values))
print('-------------------------------------------')


#원핫 인코딩
import numpy as np
onehot = np.eye(len(datas)) #정방행렬?
print(onehot, ' ', type(onehot)) #단어를 숫자화
print('-------------------------------------------')

#레이블 인코딩 : 클래스 사용
from sklearn.preprocessing import LabelEncoder
datas = ['python', 'lan', 'program', 'computer', 'say']
encoder = LabelEncoder().fit(datas)
values = encoder.transform(datas)

print(values, ' ', type(values), np.sort(values))
print(encoder.classes_)
print('-------------------------------------------')

#원핫 인코딩 : 클래스 사용
from sklearn.preprocessing import OneHotEncoder
labels = values.reshape(-1, 1)
print(labels, ' ', labels.shape)
onehot = OneHotEncoder().fit(labels)
onehotValues = onehot.transform(labels)
print(onehotValues.toarray())
print('-------------------------------------------')

#밀집 표현 : 단어마다 고유한 일련번호를 메겨서 사용하는 것이 아니라, 유사한 단어들을 비슷한 방향과 힘의 벡터를 갖도록 변환해 사용
#word2vec : 단어의 의미를 다차원 공간에 실수로 벡터화하는 분산 표현 기법. 단어간 유사성을 표현 가능

from gensim.models import word2vec #밀집벡터

sentence = [['python', 'lan', 'program', 'computer', 'say']] #중첩 리스트로 입력
model = word2vec.Word2Vec(sentence, vector_size=30, min_count=1) #size or vector_size 데이터의 크기에 따라 얼마나 줘도 상관 없음
#min_count는 단어 빈도수
print(model)

word_vectors = model.wv

#내옹을 볼 때는 이렇게 봐야함
print('word_vectors : ', word_vectors) #객체를 만들어줌
print('word_vectors_index : ', word_vectors.key_to_index) #{'say': 0, 'computer': 1, 'program': 2, 'lan': 3, 'python': 4}
print('word_vectors_index : ', word_vectors.key_to_index.keys()) #dict_keys(['say', 'computer', 'program', 'lan', 'python'])
print('word_vectors_index : ', word_vectors.key_to_index.values()) #dict_values([0, 1, 2, 3, 4])

vocabs = word_vectors.key_to_index.keys()

word_vectors_list = [word_vectors[v] for v in vocabs]

print(word_vectors_list[0], len(word_vectors_list[0])) #차원의 크기는 vector_size의 크기
print(word_vectors_list[1], len(word_vectors_list[1]))
print('-------------------------------------------')

#두 단어 사이의 유사도를(cos으로) 보여줌 - 두 벡터가 닮은 정도를 정량적으로 (-1 ~ 1) 나타낼 수 있다.
#다른 방식으로는 각각의 단어들 사이에 관계를 확인할 수가 없다.
print(word_vectors.similarity(w1='python', w2='lan'))
print(word_vectors.similarity(w1='python', w2='say'))

#시각화
import matplotlib.pyplot as plt

def plot_func(vocabs, x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    for i, v in enumerate(vocabs):
        plt.annotate(v, xy=(x[i], y[i]))
        
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
xys = pca.fit_transform(word_vectors_list)
xs = xys[:, 0]
ys = xys[:, 1]
plot_func(vocabs, xs, ys)
plt.show()



















