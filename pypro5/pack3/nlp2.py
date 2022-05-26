#웹 뉴스 자료 읽어 형태소 분석 후 word2vec을 이용하여 단어 간 유사도 확인하기
import pandas as pd
from konlpy.tag import Okt
from pyreadline.lineeditor import lineobj

okt = Okt()

with open('news.txt', mode='r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print(len(lines))

#형태소 분석 후 명사만 추출해 단어별 빈도수를 dict타입으로 추출 -> {'자동차' : 5....}
wordDic = {} 

for line in lines:
    datas = okt.pos(line) #품사 태깅
    #print(datas) #
    for word in datas:
        if word[1] == 'Noun':
            #print(word[0])
            if not(word[0] in wordDic):
                wordDic[word[0]] = 0
            
            wordDic[word[0]] += 1
print(wordDic)

#배열로 담겨있는 wordDic의 값을 언급 순서대로 sort하기
keys = sorted(wordDic.items(), key = lambda x:x[1], reverse = True) #디센딩 솔트
print(keys)
print('-------------------------------------------')

wordList = []
countList = []

for word, count in keys[:20]: #sort한 배열의 20개만 담기
    wordList.append(word)
    countList.append(count)

df = pd.DataFrame()
df['word'] = wordList
df['count'] = countList
print(df)
print('-------------------------------------------')

#두 글자 이상의 데이터를 읽어 파일로 저장
result = []

with open('news.txt', mode='r', encoding='utf-8') as f:
    lines = f.read().split('\n')

    for line in lines:
        datas = okt.pos(line, stem=True) #stem=True 원형 어근 출력. 한가한 -> 한가하다 이런식으로 바꿔주는 기능
        imsi = []
        for word in datas:
           if not word[1] in ['Verb', 'None','Number', 'Alpha', 'Foreign', 'Josa', 'Punctuation', 'Modifier', 'Determiner']:
               if len(word) >= 2:
                   imsi.append(word[0])
        #print(imsi)
        imsi2 = (" ".join(imsi).strip())          
        result.append(imsi2)
print(result)

fileName = 'news2.txt'
with open(fileName, 'w', encoding='utf-8') as fw:
    fw.write('\n'.join(result))

print('저장 성공')
print('-------------------------------------------')
 

#word2vec로 밀집벡터를 만든 후 단어 유사도 확인
from gensim.models import word2vec

lineObj = word2vec.LineSentence(fileName)

model = word2vec.Word2Vec(sentences=lineObj, vector_size=100, min_count=1, sg=0, window=10)

print(model)

print(model.wv.most_similar(positive=['전기차']))
print(model.wv.most_similar(positive=['전기차'], topn=3))
print(model.wv.most_similar(positive=['전기차', '메르세데스'], topn=3))
print(model.wv.most_similar(negative=['전기차']))


