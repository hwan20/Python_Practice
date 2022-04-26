#위키백과 사이트에서 검색단어 관련 글 스크래핑 후 형태소 분석
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse #한글 인코딩용 모듈
import pandas as pd

okt = Okt() 

para = parse.quote('이순신') #이순신이라는 단어를 인코딩 하기 위해 모듈을 임폴트 해줘야 함
#print(para) #'이순신' 이라는 단어를 인코딩한 것

#이 검색단어는 키보드에서 받을 수도 있다고 가정
url = "https://ko.wikipedia.org/wiki/"+para #'ascii' codec can't encode characters 이순신이 아닌 인코딩한 데이터를 넣어줘야 함
#url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'lxml')
#print(soup)

#한글 형태소 분석으로 명사만 추출해 기억장소에 담기
wordlist = []

for item in soup.select("div#mw-content-text > div > p"):
    if item.string != None: #string이 아닌 Null은 빠짐
        #print(item.string)
        wordlist += okt.nouns(item.string) #명사만 넣음

print('wordlist 출력 : ', wordlist)
print('단어 수 : ', len(wordlist))
print('중복 제거 후 단어 수 : ', len(set(wordlist)))

print()
word_dict = {} #{"이순신" : 5...}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1 #이순신이 있으면 1이 누적?
    else:
        word_dict[i] = 1 #

print('word_dict 출럭 : ', word_dict)


#DataFrame에 담기
print('------------------------')
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head(3))
print()

df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
print(df2)
df2 = df2.T
df2.columns = ['단어', '빈도 수']
print(df2)

#파일로 저장
df2.to_csv('이순신.csv', sep=',', index=False)
df3 = pd.read_csv('이순신.csv')
print(df3)




