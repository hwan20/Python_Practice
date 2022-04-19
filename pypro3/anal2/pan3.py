#함수
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan], [7, 4.5], [np.NaN, np.NAN], [0.5, -1]]) #1열, 2열 순으로 입력한 값을 출력
df.columns = ['one', 'two']
print(df)
print('-------------')
print(df.drop(1)) #1행을 삭제해서 출력
print('-------------')
print(df.isnull()) #NaN값이 있으면 True
print('-------------')
print(df.notnull()) #NaN값이 있으면 False
print('-------------')
print(df.dropna()) #데이터 중에 NaN이 하나라도 있는 행 삭제   any와 같다
print('-------------')
print(df.dropna(how='any')) #데이터 중에 NaN이 하나라도 있는 행 삭제
print('-------------')
print(df.dropna(how='all')) #데이터 중에 NaN이 모두 있는 행만 삭제
print('-------------')
print(df.dropna(subset=['one'])) #데이터의 특정 열 값 중 NaN이 있는 행 삭제
print('-------------')
print(df.dropna(axis = 'rows')) #데이터의 행에 NaN이 있으면 해당 행 삭제
print('-------------')
print(df.dropna(axis = 'columns')) #데이터의 열에 NaN이 있으면 해당 열 삭제
print('-------------')
print(df.fillna(0)) #데이터의 NaN값을 0으로 채움, 평균 또는 대표값으로 채울 수도 있다
print('-------------')

print(df)
print('-------------')
print(df.sum()) #열에 있는 데이터의 합을 구함
print('-------------')
print(df.sum(axis=0)) #열에 있는 데이터의 합을 구함
print('-------------')
print(df.sum(axis=1)) #행에 있는 데이터의 합을 구함
print('-------------')
print(df.mean(axis=0)) #열에 있는 데이터의 평균을 구함   NaN은 제외
print('-------------')
print(df.mean(axis=1)) #행에 있는 데이터의 평균을 구함
print('-------------')
print(df.idxmax()) #가장 큰 값의 인덱스를 반환
print('-------------')
print(df.max()) #데이터의 가장 큰 값을 반환
print('-------------')
print(df.describe()) #요약 통계량
print('-------------')
print(df.info()) #df의 구조를 볼 수가 있다
print('-------------')

words = Series(['봄', '여름', '봄'])
print(words.describe()) #숫자로 썻을 때랑 문자로 썻을 때가 다르게 나옴
print('-------------')
#print(words.info()) #Series는 info가 없다








