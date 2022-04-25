#Pandas : 고수준의 자료 구조(Series, DataFrame)를 지원
#축약 연산, SQL 처리, 시계열 데이터 처리, 시각화 등등....

import pandas as pd
#from pandas import Series
import numpy as np

#Seires : 일련의 데이터를 담을 수 있는 1차원 배열과 비슷한 자료구조를 가지며, 색인을 지원함

obj = pd.Series([3, 7, -5, 4]) #데이터 구조가 같아야 되기 때문에 하나의 데이터 타입이 실수나 문자열로 바뀌면 전체가 다 바뀜 - 배열과 비슷한 자료 구조
#list, tuple type 가능 TypeError : 'set' type is unordered - set은 순서가 없기 때문 (인덱스(색인)를 지원하니)

print(obj, type(obj)) #dtype: int64 <class 'pandas.core.series.Series'>

obj2 = pd.Series([3, 7, -5, 4], index = ['a', 'b', 'c', 'd'])
#생성시 색인을 지정

print(obj2)

print(sum(obj2), obj2.sum(), np.sum(obj2))
#python의 함수와 pandas, numpy의 함수. pandas와 numpy의 함수는 같다 주로 pandas나 numpy의 함수를 사용

print(obj2.values) #obj2의 요소값만 가져올 수가 있다
print(obj2.index) #obj2의 인덱스만 가져올 수가 있다   dtype = index

#인덱싱, 슬라이싱
print('-------------')
print(obj2)
print('-------------')
print(obj2[1])
print('-------------')
print(obj2['b'])
print('-------------')
print(obj2[['b']]) #b    7   series값을 모두 얻음
#print(obj2[[7]]) #IndexError: index 7 is out of bounds for axis 0 with size 4
print(obj2[['a', 'b']]) #a    3 , b    7
print(obj2['a': 'b']) #a    3 , b    7

print('-------------')
print(obj2[2]) #-5
print('-------------')
print(obj2[1:4]) #인덱스 1번~4번
print('-------------')
print(obj2[[2, 1]]) #인덱스 
print('-------------')
print(obj2 > 1) #요소의 값이 1보다 크면 True 작으면 False
print('-------------')
print('a'in obj2) #인덱스 a가 obj2안에 있으면 True
print('e'in obj2) #인덱스 e가 obj2안에 없으면 False

print('-------------')
#dict type으로 Series 객체 생성
names = {'mouse':5000, 'keyboard':25000, 'monitor':550000}
print(names, type(names)) #<class 'dict'> dict타입
print('-------------')

obj3 = pd.Series(names)
print(obj3, type(obj3)) #<class 'pandas.core.series.Series'> Series타입
print('-------------')

obj3.index = ['마우스', '키보드', '모니터'] #설정한 index(key) 값을 바꿀 수 있다
print(obj3)
print('-------------')

print(obj3['마우스']) #인덱스 값으로 요소를 빼올 수 있다
print('-------------')

obj3.name = '상품가격' #Series에 이름도 붙일 수가 있다
print(obj3)
print('-------------')

print('\n~~~DataFrame~~~~~~~~~~~~~~~~~~')
#DataFrame : 표 모양(2차원)의 자료구조로 여러 개의 칼럼(열)을 갖는다.
from pandas import DataFrame
df = DataFrame(obj3)
print(df, type(df)) #<class 'pandas.core.frame.DataFrame'> DataFrame타입
print('-------------')

data = {
    'irum' : ['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso' : ('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
    'nai': [23, 25, 33, 30, 35]
}
#데이터는 Local, 데이터베이스, 파일, web(SNS, HomePage), 네트워크 장비 등 다양한 곳 에서 얻을 수가 있다

print(data, type(data)) #<class 'dict'>
print('-------------')

frame = DataFrame(data) #<class 'pandas.core.frame.DataFrame'>
print(frame, type(frame)) #DataFrame은 배열과 비슷한 모습
print('-------------')

print(frame['irum'], type(frame['irum'])) #데이터 하나를 뽑으면 Series, Series가 모이면 DataFrame
print('-------------')
print(frame.irum)
print('-------------')

print(DataFrame(data, columns = ['juso', 'irum', 'nai']))
#칼럼명 대로 데이터 순서가 바뀌지만 테이블에서 읽어올 때 칼럼명 대로 읽어올 수가 있으니 크게 중요하지 않을 수도 있다
print('-------------')

frame2 = DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'], index = ['a', 'b', 'c', 'd', 'e'])
#frame2.columns=['irum', 'nai', 'juso', 'tel'] 이렇게도 줄 수가 있다
#frame2.index = ['a', 'b', 'c', 'd', 'e']
print(frame2)
print('-------------')

frame2["tel"] = "1111-1111" #해당 칼럼의 모든 행에 적용된다
print(frame2)
print('-------------')

val = pd.Series(['222-2222', '333-3333', '444-4444'], index = ['b', 'c', 'e'])
print(val)
print('-------------')

frame2['tel'] = val #frame2의 tel columns의 행에 정해진 인덱스에 val이 덮어씌어짐
print(frame2) #덮어씌어진 거라 빈 인덱스의 데이터는 NaN이 나옴
print('-------------')

print(frame2.T) #전치 - 행열의 위치를 변경
print('-------------')

print(frame2.values) #데이터 프레임의 값을 빼오면 matrix의 모양을 띈다
print('-------------')

print(frame2.values[0]) #데이터의 0행을 빼옴
print(frame2.values[0:2]) #데이터의 0행부터 1행까지 빼옴
print(frame2.values[0,1]) #데이터의 0행, 1열을 빼옴
print('-------------')

frame3 = frame2.drop('d') #행 삭제
#frame3 = frame2.drop('d', axis = 0) 과 같음 
print(frame3)
print('-------------')

#frame4 = frame2.drop('tel') KeyError: "['tel'] not found in axis"  axis는 기본이 행이라 찾지를 못함
frame4 = frame2.drop('tel', axis = 1)
print(frame4)
print('-------------')

print(frame2)
print(frame2.sort_index(axis = 0, ascending = False)) #ascending 기본은 True False로 하면 인덱스가 내림차순으로 나온다
print('-------------')

print(frame2.sort_index(axis = 1, ascending = True)) #행 칼럼의 순서를 오름차순으로 바꿈
print('-------------')

print(frame2.rank(axis = 0)) #오름차순으로 순위를 매길 수 있다 NaN은 제외
print('-------------')

print(frame2['juso'].value_counts())
print('-------------')

data = {
    'juso' : ['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon' : [23, 25, 15]
}

print(data) #dict 타입
print('-------------')

fr = DataFrame(data)
print(fr)
print('-------------')

result1 = pd.Series([ju.split()[0] for ju in fr.juso])
print(result1)
print('----------------------------------------------')
print(result1.values)
print('-------------')
print(result1.value_counts())
print('-------------')

result2 = pd.Series([ju.split()[1] for ju in fr.juso])
print(result2)
print('-------------')
print(result2.values)
print('-------------')
print(result2.value_counts())
print('-------------')




