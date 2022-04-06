#멀티 프로세싱 처리를 위한 웹 스크래핑

#멀티 프로세싱 사용 X
#https://beomi.github.io/beomi.github.io_old/ 사이트의 컨텐츠를 scraping함

import requests
from bs4 import BeautifulSoup as bs
import time

from multiprocessing import Pool



#웹 페이지 안에 들어가서 제목을 가져오는 것

def get_link(): #제목 a tag 읽기
    data = requests.get("https://beomi.github.io/beomi.github.io_old/").text #이건 나중에 설명
    soup = bs(data, "html.parser") #나중에 설명........ html 혹은 parser만 됨
    my_titles = soup.select(
            " h3 > a "
    ) #css태그 그대로 사용
    
    data = []
    for title in my_titles:
        data.append(title.get("href"))

    return data

def get_content(link):
    #print(link) #링크가 잘 나오나 테스트 해봄
    abs_link = "https://beomi.github.io" + link
    #print(abs_link) #원하는 웹 사이트에서 link를 빼왔을 때 앞에 https://beomi.github.io 가 없어 붙여줌
    data = requests.get(abs_link).text
    soup = bs(data, "html.parser")
    
    #가져온 데이터로 뭔가를 할 수 있다 - 지금은 사용 안 함 지금은 pool을 알아보기 위해 잠시 사용
    print(soup.select("h1")[0].text) #첫 번째 h1 tag안에 있는 문자열을 출력
    
if __name__ == "__main__":
    startTime = time.time()
    """
    #print(get_link()) #Web의 link들을 list형태로 가져옴
    #print(len(get_link())) #Web에 있는 link들의 갯수
    
    for link in get_link():
        get_content(link)    #3.79초
    """
    pool = Pool(processes = 4) #병렬처리 1.65초 훨씬 빠름
    pool.map(get_content, get_link()) #get_link의 갯수만큼 get_content를 실행
    
    print("----- %s 초 -----"%(time.time()-startTime))
    
    
    

