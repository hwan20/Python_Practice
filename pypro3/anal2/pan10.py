#네이버의 영화 랭킹 읽기

import urllib.request as req
from bs4 import BeautifulSoup

#방법 1 : urllib.request
import urllib.request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
data = urllib.request.urlopen(url)

soup = BeautifulSoup(data, "lxml")
##old_content > table > tbody > tr:nth-child(2) > td.title > div
#old_content > table > tbody > tr:nth-child(2) > td.title > div
print(soup.select("div.tit3"))
print('-------------')

print(soup.select("div[class=tit3]"))
print('-------------')

print(soup.find_all("div", {'class':'tit3'}))
print('-------------')

print(soup.findAll("div", {'class':'tit3'}))
print('-------------')

#위 4개가 다 같은 것을 출력

for tag in soup.findAll("div", {'class':'tit3'}):
    print(tag.text.strip())
print('-------------')

#방법 2: requests
import requests
data = requests.get(url).text
soup2 = BeautifulSoup(data, 'lxml')
m_list = soup.find_all('div', 'tit3')
#print(m_list)

count = 1
for i in m_list:
    title = i.find('a')
    print(str(count)+"위 : ", title.string)
    count += 1

