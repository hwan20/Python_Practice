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













