#인터넷에서 특정 단어로 검색된 문서를 읽어 형태소 분석 후 명사만 추출해 워드 클라우드 형태로 실행

#워드 클라우드를 하기 위해서는 설치해야 할 것들이 있다
#pip install pygame -> pygame하기 위해서는 창이 뜨는데 그 창을 사용하기 위해
#pip install simplejson
#pip install pytagcloud #이 프로그램을 사용하기 위해 위에 것들을 설치
#설치하면 python의 lib -> sitepackage에 설치됨. 이것을 eclipse에서 불러오는 것

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from konlpy.tag import Okt
from collections import Counter #단어 갯수를 세어주는 모듈
import pytagcloud
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


"""
매번 치기 귀찮으니 주석처리
keyword = input('검색어 입력 : ')
print(keyword) #ex)열병식
print(quote(keyword)) #ex) %EC%97%B4%EB%B3%91%EC%8B%9D
"""

keyword = quote('마스크')

#신문사 검색 기능 이용
url = "https://www.donga.com/news/search?query=" + keyword
#print(url)
#https://www.donga.com/news/search?query=%EB%A7%88%EC%8A%A4%ED%81%AC
source = urllib.request.urlopen(url)

soup = BeautifulSoup(source, 'lxml', from_encoding='UTF-8')
#print(soup)

msg = ""
for title in soup.find_all('p', 'tit'):
    title_link = title.select('a')
    #print(title_link)
    article_url = title_link[0]['href'] #a링크의 href로 들어가기 위해 href의 주소가 필요함
    #print(article_url)
    
    try:
        source_article = urllib.request.urlopen(article_url) #각 타이틀에 있는 기사 내용을 읽어온다
        soup = BeautifulSoup(source_article, 'lxml', from_encoding='UTF-8')
        contents = soup.select('div.article_txt')
        #print(contents)
        for imsi in contents:
            item = str(imsi.find_all(text=True))
            #print(item)
            msg = msg + item
        
    except Exception as e:
        pass

#print(msg)


#from konlpy.tag import Okt
#from collections import Counter

okt = Okt()
nouns = okt.nouns(msg) #문서의 문장들 중 명사만 얻어 오기
#print(nouns)

#두 글자 이상의 단어만 저장
result = []
for imsi in nouns:
    if len(imsi) > 1:
        result.append(imsi)

#print(result)
count =Counter(result)
tag = count.most_common(100) #많이 언급된 상위 50개만 tuple type으로 작업에 참여
print(tag)

#import pytagcloud #워드클라우드를 만들기 위해 필요한 모듈
taglist = pytagcloud.make_tags(tag, maxsize=100)
print('taglist : ', taglist)

pytagcloud.create_tag_image(taglist, output='word.png', size=(1000,600),
                            background=(0, 0, 0), fontname='korean', rectangular=False) #background 기본은 255, 255, 255 하얀색
#png파일이 한글로 만들어졌지만 한글이 깨지는 상황이 발생
#pytagcloud가 설치된 곳으로 가서 font에 한글을 추가해야 함 -> json 형식의 파일에 추가

#이미지 읽기
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#%matplotlib inline    #jupyter에서 선언하면 show() 안 해도 된다

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()





