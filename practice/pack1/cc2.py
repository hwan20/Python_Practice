import urllib.request as req 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Chrome 웹 드라이버 생성 파일이 있는 경로 작성
driver = webdriver.Chrome('C:\work/chromedriver.exe')


#div.c_prd_name.c_prd_name_row_1 > a > strong
#driver.get('https://google.com')
driver.get('https://search.11st.co.kr/Search.tmall?kwd=%25EC%258B%25A0%25EB%259D%25BC%25EB%25A9%25B4')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())


