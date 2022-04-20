# 웹 문서 읽기
#import requests 
import urllib.request as req #둘 중 어느걸 사용해도 괜찮다
from bs4 import BeautifulSoup

#위키백과 사이트에서 '이순신'으로 검색된 자료 읽기
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url) #<http.client.HTTPResponse object at 0x0000027CC53FA220>
print(wiki) #저장된 url의 데이터가 아닌 인스턴스를 보여줌
print('-------------')
#print(wiki.read()) #

soup = BeautifulSoup(wiki,'html.parser') #저장된 객체를 BeSoup 객체로 읽어옴
#print(soup)
print('-------------')

#mw-content-text > div.mw-parser-output > p:nth-child(5)   selector 복사해온거
print(soup.select_one("div.mw-parser-output > p")) #맨 위의 p태그만 가져옴
#print(soup.select("div.mw-parser-output > p")) #p태그 전체를 가져옴
print('-------------')

ss = soup.select("div.mw-parser-output > p > b") #p태그 안에 있는 b태그만 출력
#ss = soup.select("div.mw-parser-output > p") #p태그 안에 있는 p태그만 출력 비어있는 것은 if문을 통해 공백으로 처리 가능
for s in ss:
    if s.string != None:
        print(s.string)
print('-------------')

url2 = "https://news.daum.net/society#1"
daum= req.urlopen(url2)

soup2 = BeautifulSoup(daum, 'lxml')
#body > div.direct-link
print(soup2.select_one("body > div.direct-link"))
#print(soup2.select_one("body > div.direct-link").string) #None이 나옴
print('-------------')
print(soup2.select_one("body > div.direct-link > a").string)
print('-------------')

datas = soup2.select("div.direct-link > a")
print(datas)
print('-------------')

for i in datas:
    href = i.attrs['href']
    ss = i.string
    print("href:%s, text:%s" %(href, ss))
print('-------------')

datas = soup2.findAll('a')
#print(datas)
for i in datas[:10]:
    href = i.attrs['href']
    ss = i.string
    print("href:%s, text:%s" %(href, ss))
print('-------------')



