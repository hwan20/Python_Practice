#BeautifulSoup 객체의 find(), select() 연습
from bs4 import BeautifulSoup

html_page = """
<html>
<body>
<h1> 제목 태그 </h1>
<p> 웹문서 읽기 </p>
<p> 파이썬 라이브러리 사용 </p>
</body>
</html>
"""

print(html_page, type(html_page)) #<class 'str'>

soup = BeautifulSoup(html_page, 'html.parser') #BeautifulSoup 객체 생성
print(soup, type(soup)) # class 'bs4.BeautifulSoup'>
print('-------------')

h1 = soup.html.body.h1 #DOM형태로 h1을 찾아감
print(h1)
print("h1:", h1.string) #태그안에 들어있는 텍스트만 추출
print("h1:", h1.text)
print('-------------')

p1 = soup.html.body.p #DOM형태로 p를 찾아감
print(p1)
print("h:", p1.string) #하나의 p밖에 안 나옴
print("h:", p1.text) 
print('-------------')

p2 = p1.next_sibling.next_sibling #next_sibling을 하나만 사용하면 </p>, 2개를 사용해야함
print(p2)
print('-------------')

#이렇게도 할 수는 있지만 많이 귀찮고 복잡해짐 그래서 사용하는게 'find()'
print("-----find()사용-----")

html_page2 = """
<html>
<body>
<h1 id="title"> 제목 태그 </h1>
<p> 웹문서 읽기 </p>
<p id="my" class="our"> 파이썬 라이브러리 사용 </p>
</body>
</html>
"""

soup2 = BeautifulSoup(html_page2, 'lxml') #BeautifulSoup 객체 생성
print(soup2.p, ' ', soup2.p.string) #직접 최초 p tag 선택
print(soup2.find('p').string) #find는 기본적으로 최초의 p tag를 찾아간다
print(soup2.find('p', id="my").string) #id가 my인 p태그 추출
print('-------------')
#print(soup2.find(['p', 'h1']))
print(soup2.find(id='my').string)
print(soup2.find(id='title').string)
print(soup2.find(class_='our').string) #class는 class_로 줘야한다
print('-------------')
print(soup2.find(attrs={'class':'our'}).string) #이렇게 하는 방법도 있다
print(soup2.find(attrs={'id':'title'}).string)

#find는 첫 번째 p태그 밖에 얻지 못 한다 전체를 추출하고 싶으면 'findAll()'을 사용
print("-----findall(), findAll()사용-----")

html_page3 = """
<html>
<body>
<h1 id="title"> 제목 태그 </h1>
<p> 웹문서 읽기 </p>
<p id="my" class="our"> 파이썬 라이브러리 사용 </p>
<div>
    <a href="https://www.naver.com">네이버</a>
    <a href="https://www.daum.net">다음</a>
</div>
</body>
</html>
"""

soup3 = BeautifulSoup(html_page3, 'lxml') #
print(soup3.find_all(['a'])) #
print(soup3.find_all(['a', 'p'])) #
print(soup3.findAll(['a'])) #
print(soup3.find_all('a')) #[] 는 집합을 뽑아내는 것
print('-------------')

links = soup3.find_all('a')
for i in links:
    href = i.attrs['href']
    text = i.string
    print(href, ' ', text)

print('-------------')
import re #정규표현식

links2 = soup3.find_all(href = re.compile(r'^https')) #href가 https로 시작하는 것만 뽑아오기
print(links2)

#find와 selector 섞어서 사용하면 좋음
print("-----셀렉터(css의 selector)사용-----")

html_page4 = """
<html>
<body>
<div>
    <a href="https://www.sbs.com">sbs</a>
</div>
<div id="hello">
    <b>파이썬</b>
    <a href="https://www.kbs.com">kbs</a>
    <a href="https://www.naver.com">네이버</a>
    <span>
        <a href="https://www.tvn.com">tvn</a>
    </span>
</div>
<span>
    <a href="https://www.mbc.com">mbc</a>
</span>
<ul class="world">
    <li>안녕</li>
    <li>반가워</li>
</ul>
<p> 웹문서 읽기 </p>
<p id="my" class="our"> 파이썬 라이브러리 사용 </p>
<div id="hi" class="good">
    second div
    <a href="https://www.daum.net">다음</a>
</div>
</body>
</html>
"""

soup4 = BeautifulSoup(html_page4, 'lxml')
aa = soup4.select_one("div") #첫 번째 div의 내용을 추출 
print(aa)
print('-------------')

bb = soup4.select_one("div#hello") #id가 hello인 div의 내용을 추출
print(bb)
print(bb.string)
print('-------------')

cc = soup4.select_one("div#hello > a") #div의 hello 중에서 a태그
print(cc)
print(cc.string)
print('-------------')

d = soup4.select_one("div#hi > a") #div의 hi 중에서 a태그
print(d)
print(d.string)
print('-------------')

dd = soup4.select("div#hello > a") #div의 hello 자식 중에 a태그 복수 선택
print(dd)
print('-------------')

ee = soup4.select("div#hello a") #div의 hello 자식과 자손 모두 a태그 복수 선택
print(ee)
print('-------------')

ff = soup4.select("ul.world > li") #ul태그의 class가 world중 li태그 복수 선택
print(ff)
print('-------------')

msg = list()
for k in ff:
    print("li : ", k.string) #ff의 내용을 뽑을 수 있다
    msg.append(k.string)
print('-------------')

import pandas as pd
df = pd.DataFrame(msg, columns = ['자료']) #list에 담은 msg를 DataFrame형태로 뽑을 수 있다
print(df)


