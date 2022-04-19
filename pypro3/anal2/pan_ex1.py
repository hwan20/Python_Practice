#문제 1
#a) 표준 정규분표를 따르는 9X4형태의 DataFrame를 생성
#np.random.randn(9, 4)
#b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정
#c) 각 칼럼의 평균을 구하기 mean()함수와 axis속성 사용

from pandas import Series, DataFrame
import numpy as np

#a)
data = np.random.randn(9, 4)
print(data)
df = DataFrame(data)
print(df)

#df2 = DataFrame(np.random.randn(9, 4))
#print(df2)

#b)
df = DataFrame(data, columns = ['No1', 'No2', 'No3', 'No4'])
print(df)

#c)
print(df.mean(axis=0))
print(df.mean(axis=1))

print('-------------')
#문제 2
#      numbers
#    a  10
#    b  20
#    c  30
#    d  40
#a) DataFrame을 위와 같은 자료로 만들기 column name은 numbers, row name은 a~d이고 값은 10~40
#b) c row의 값을 가져오기
#c) a, d row들의 값을 가져오기
#d) numbers의 합을 구하기
#e) numbers의 값들을 각각 제곱하여 아래 결과가 나오게 하기
#      numbers
#    a  100
#    b  400
#    c  900
#    d  1600
#f) floats라는 이름의 칼럼을 추가하고 값은 1.5, 2.5, 3.5, 4.5
#      numbers    floats
#    a      10        1.5
#    b      20        2.5
#    c      30        3.5
#    d      40        4.5
#g) names라는 이름의 칼럼을 추가하고 아래와 같이 출력하게 하기. Series클래스 사용
#      names
#    d  길동
#    a  오정
#    b  팔계
#    c  오공


#a)
df2 = DataFrame([[10], [20], [30], [40]], index = ['a', 'b', 'c', 'd'], columns = ['numbers'])
print(df2)
#df2.index = ['a', 'b', 'c', 'd']
#df2.columns = ['numbers']
print(df2)

#b) 
print(df2.loc['c'])

#c)
print(df2.loc['a':'c'])

#d)
print(df2.sum(axis=0))

#e)
print(df2 * df2)
#print(df2 ** 2)

#f)
df2['floats'] = [1.5, 2.5, 3.5, 4.5]
print(df2)
#df2.insert(2, 'floats2', [1.5, 2.5, 3.5, 4.5])
#print(df2)

#g)
df2['names'] = Series(['길동', '오정', '팔계', '오공'], index = ['d', 'a', 'b', 'c'])
print(df2)






