#일정 시간마다 웹 문서를 스크래핑 하기
import datetime
import time
import urllib.request as req
from bs4 import BeautifulSoup

def working_func():
    url = "https://finance.naver.com/marketindex/"
    data = req.urlopen(url)
    soup = BeautifulSoup(data, 'lxml')
    price = soup.select_one("div.head_info > span.value").string
    print("미국 USD : ", price)
    
    t = datetime.datetime.now()
    #print(t) 현재 시간 출력
    
    #usd폴더에 일정 시간마다 저장
    fname = "./usd/" + t.strftime("%Y-%m-%d-%H-%M-%S") + '.txt'
    print(fname)
    with open(fname, mode = 'w') as f:
        f.write(price)

while True:
    working_func()
    time.sleep(3)


