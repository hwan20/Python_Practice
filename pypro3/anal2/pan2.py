from pandas import Series, DataFrame

data = Series([1, 3, 2], index = (1, 4, 2))
print(data)
print('-------------')

#인덱스 재배치
data2 = data.reindex((1, 2, 4)) #행에 대한 순서 재배치
print(data2)
print('-------------')

data3 = data2.reindex([0, 1, 2, 3, 4, 5]) #대응 값이 없는 인덱스는 결측값이 됨
print(data3)
print('-------------')

data3 = data2.reindex([0, 1, 2, 3, 4, 5], fill_value = 777) #대응 값이 없는 인덱스는 777로 채움
print(data3)
print('-------------')

data3 = data2.reindex([0, 1, 2, 3, 4, 5], method = 'ffill') #앞의 인덱스의 값으로 NaN을 채움
print(data3)
print('-------------')

data3 = data2.reindex([0, 1, 2, 3, 4, 5], method = 'pad') #ffill와 같음
print(data3)
print('-------------')

data3 = data2.reindex([0, 1, 2, 3, 4, 5], method = 'bfill') #뒤의 인덱스의 값으로 NaN을 채움
print(data3)
print('-------------')

data3 = data2.reindex([0, 1, 2, 3, 4, 5], method = 'backfill') #뒤의 인덱스의 값으로 NaN을 채움
print(data3)
print('-------------')

import numpy as np
df = DataFrame(np.arange(12).reshape(4,3), index=['1월', '2월', '3월', '4월'], columns = ['강남', '강북', '서초'])
print(df)
print('-------------')

print(df['강남']) #칼럼 이름이 강남인 열만 출력
print('-------------')

print(df['강남'] > 3) #칼럼 이름이 강남인 열 중에 3보다 크면 True
print('-------------')

print(df[df['강남'] > 3]) #칼럼 이름이 강남ㅁㄴㅇㅁㄴㅇㅁㅇㅁㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅇㅂ쟈ㅓㅐㅈ댜ㅐㅔㅂ
print('-------------')

df[df < 3] = 0 #df의 data 값이 3보다 작으면 0으로 바꿈
print(df)
print('-------------')

print('슬라이싱 관련 메소드 : loc() - 라벨을 지원, iloc() - 숫자를 지원')
print(df['강남']) #칼럼 명이 강남인 열만 슬라이싱
print('-------------')

#복수 인덱싱 loc
print(df.loc['3월']) #3월 행만 출력
print('-------------')
print(df.loc['3월'], ) #3월 행만 출력
print('-------------')
print(df.loc['3월', ]) #3월 행만 출력
print('-------------')
print(df.loc['3월', :]) #3월 행만 출력
print('-------------')
print(df.loc[:'3월']) #3월 이하 행 모든 열 출력
print('-------------')
print(df.loc[:'3월', ['서초']]) #3월 이하 행과 서초의 모든 열 출력
print('-------------')

#복수 인덱싱 iloc
print(df.iloc[2]) #2행 출력
print('-------------')
print(df.iloc[2], ) #2행 출력
print('-------------')
print(df.iloc[2, :]) #2행 출력
print('-------------')
print(df.iloc[:3]) #3미만 행 출력
print('-------------')
print(df.iloc[:3, 2]) #3미만 행과 2열 출력
print('-------------')
print(df.iloc[1:3, 1:3]) #1행부터 2행까지 1열부터 2열까지 출력
print('-------------')

#연산
s1 = Series([1, 2, 3], index = ['a', 'b', 'c'])
s2 = Series([4, 5, 6, 7], index = ['a', 'b', 'd', 'c'])
print(s1)
print('-------------')
print(s2)
print('-------------')
print(s1 + s2) #같은 인덱스 명 끼리 더함, 없는 인덱스는 NaN이 출력   -, *, /
print('-------------')
print(s1.add(s2)) #sub, mul, div
print('-------------')

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'), index=['서울', '대전', '부산']) #columns=list('kbs') kbs가 슬라이싱 돼서 k, b, s로 칼럼 명이 됨
print(df1)
print('-------------')

df2 = DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'), index=['서울', '대전', '제주', '광주'])
print(df2)
print('-------------')

print(df1 + df2) #index명이 일치하는 행만 더하고 나머지는 NaN이 출력
print(df1.add(df2, fill_value = 0)) #index명이 일치하는 행만 더하고 나머지는 0으로 채움




