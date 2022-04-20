#BeautifulSoup으로 xml 문서 처리

#xml로 데이터 저장, 레이아웃 작성, 안드로이드나 아이폰 앱 작성할 때 xml로 작성, 환경설정 xml
#데이터를 주고 받을 때도 xml을 사용하지만 요즘은 json에 조금 밀리는 경향

#DOM을 쓰기 싫어서 BeautifulSoup을 씀
from bs4 import BeautifulSoup
import pandas as pd
from pandas.tests.frame.methods.test_sort_values import ascending

with open('../testdata/my.xml', mode = 'r', encoding='UTF-8') as f:
    xmlfile = f.read()

print(xmlfile, type(xmlfile)) #<class 'str'>
print('-------------')

soup = BeautifulSoup(xmlfile, 'lxml')
print(soup, type(soup)) #<class 'bs4.BeautifulSoup'>
print('-------------')

print(soup.prettify()) #HTML 형식을 유지한체 보여줌
print('-------------')

itemTag = soup.findAll('item')
print(itemTag[0]) #item태그의 1번째
print('-------------')

nameTag = soup.findAll('name')
print(nameTag[0]['id']) #name태그의 1번째 id만을 가져옴
print('-------------')

for i in nameTag: #nameTag의 갯수만큼 반복하며 id를 출력함
    print(i['id'])
print('-------------')

for i in itemTag:
    nameTag = i.findAll('name')
    for j in nameTag:
        print('id : ' + j['id'] + ', name : ' + j.string)
        tel = i.find('tel')
        print('tel : ' + tel.string)
    
    for j in i.find_all('exam'):
        print('kor : ' + j['kor'] + ', eng : ' + j['eng'])
print('-------------')

#서울시 지원 강남구 도서관 정보 읽기
#제대로 하려면 try except 문 활용해서 해야함
try:
    import urllib.request as req
    url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
    plainText = req.urlopen(url).read().decode("UTF-8")
    #print(plainText)
    
    soup = BeautifulSoup(plainText, 'lxml')
    #print(soup)
    title = soup.find('title').string
    print(title)
    print('-------------')
    
    #wf = soup.find('wf')
    #print(wf)
    
    city = soup.find_all("city")
    #print(city)
    #print('-------------')
    
    #text만 뽑기 위해서
    cityDatas = []
    for c in city:
        cityDatas.append(c.string)
    df = pd.DataFrame()
    df['city'] = cityDatas
    #print(df)
    
    #첫째 날의 최저 온도
    tempMins = soup.select('location > province + city + data >tmn') #+(next_sibling)는 아래방향, -는 윗방향을 가르킨다 (location의 자식들)
    #print(tempMins)
    
    tempDatas = []
    for t in tempMins:
        tempDatas.append(t.string)
    df['temp_min'] = tempDatas
    df.columns = ['지역', '최저기온'] #칼럼명을 바꾸고 싶으면 작성
    print(df.head(3))
    print(df.tail(3))
    print('-------------')
    
    #df를 파일로 저장
    df.to_csv("날씨.csv", index = False)
    
    #저장된 파일을 읽기
    print(pd.read_csv("날씨.csv"))
    print('-------------')
    
    print(df[0:3], type(df)) #0~2까지 인덱싱으로 읽기   <class 'pandas.core.frame.DataFrame'>
    print(df[-3:len(df)]) #맨 뒤에서 3번째 부터 df의 길이만큼 읽기
    print('-------------')
    
    print(df.iloc[0], type(df.iloc[0])) #class 'pandas.core.series.Series'> 하나만 읽었으니
    print('-------------')
    
    print(df.iloc[0:2, :], type(df.iloc[0:2, :]))
    print(df.iloc[0:2, 0:1])
    print(df.iloc[0:2, 0:2])
    print('-------------')
    
    print(df.loc[1:3]) #loc는 안에 라벨명을 쓸 수 있다
    print(df.loc[[1, 3]]) #1행, 3행만
    print('-------------')
    
    print(df.loc[1:3, ['최저기온', '지역']]) #칼럼 순서 바꾸기
    print('-------------')
    
    print(df['최저기온'].mean()) #최저기온의 평균
    print(df['최저기온'].describe()) #최저기온 칼럼의 정보
    print('-------------')
    
    df = df.astype({'최저기온' : int}) #str타입인 최저기온을 int 타입으로 변환
    print(df.loc[df['최저기온'] >= 10]) #최저기온 10도 이상만 출력
    print('-------------')
    
    print(df.loc[(df['최저기온'] >= 10) & (df['최저기온'] <= 12)]) #최저기온이 10도 이상 12도 이하만 출력
    print('-------------')
    
    print(df.sort_values(['최저기온'], ascending=True)) #최저기온으로 오름차순 정렬
    
except Exception as e:
    print('err : ', e)




