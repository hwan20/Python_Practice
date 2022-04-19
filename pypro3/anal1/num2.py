#numpy기본 이해

import numpy as np 
#python만 깔면 numpy가 없음 lib 다운 받아야함
#우리는 아나콘다를 깔아서 자동으로 깔음

print(np.__version__) #numpy 버전

#numpy는 배열

s = 'tom' #스칼라 타입

ss = ['tom', 'james', 'oscar']

print(ss, type(ss)) #['tom', 'james', 'oscar'] <class 'list'>

ss2 = np.array(ss) #리스트를 넣으면 타입이 바뀌고, 컴마 ','가 사라짐
print(ss2, type(ss2)) #['tom' 'james' 'oscar'] <class 'numpy.ndarray'>

print("-----------list/numpy.ndarray 기억상태 구분-----------")

li = list(range(0,10)) #어떤 종류의 아이디가 10개가 있으면
print(li)
print(id(li[0]), id(li[1])) #2193115998512 2193115998544 아이디가 다 다름
#만약 아이디의 종류가 1000만개라면 1000만개의 객체가 생성되니 처리 속도도 늦고 데이터도 부담됨

print(li * 10) #list를 10번 반복한다는 뜻

#각 숫자마다 10을 곱하고 싶으면
for i in li:
    print(i * 10, end = "\n")
    
print([i * 10 for i in li])#위와 같음

print("-----------list를 ndarray로-----------")
num_arr = np.array(li)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1])) #2261281143312 2261281143312 아이디가 같아짐
print(num_arr * 10) #[ 0 10 20 30 40 50 60 70 80 90]

#python은 list의 숫자에 해당하는 객체가 각각 따로 생성되고 관리됨
#그렇기 때문에 python은 객체 안에 있는 데이터의 타입이 달라도 된다
#numpy의 list는 하나의 객체 안에 해당 리스트의 값을 한 번에 저장한다
#하나의 객체 안에 모두 관리되기 때문에 numpy의 list는 데이터 타입이 다르면 안 된다

#python은 그래서 처리 속도가 느리지만 version이 높아지면서 빨라진다
#속도 자체도 numpy의 array를 썼을 때 python보다 빠르다
#python의 list는 유연성이 좋으며 각각의 데이터 장소가 데이터 타입이 달라도 된다, 하지만 비용이 많이 든다 
#ndarray 메모리를 효과적으로 관리하지만 유연성이 떨어지지만 데이터 검색에 효과적



print()
a = np.array([1, 2, 3]) #정수로 처리됨
#a = np.array([1, 2, 3.2]) #모두 실수로 처리됨, 자료 구조를 묶어서 관리하기 때문이다
#a = np.array([1, 2, '3.2']) #모두 문자열로 처리됨, 데이터는 상위 타입을 따른다
print(a, type(a), a.dtype, a.shape, a.ndim, a.size)
#[1 2 3] <class 'numpy.ndarray'> int32 (3,) 1 3
print(a[0]) #인덱싱
print(a[1:3]) #슬라이싱
print(a[-1])

print()
b = np.array([[1, 2, 3], [4, 5, 6]]) #2차원 배열이다
print(b, type(b), b.dtype, b.shape, b.ndim, b.size)
#[[1 2 3]
# [4 5 6]] <class 'numpy.ndarray'> int32 (2, 3) 2 6
print(b[0, ]) #인덱싱
print(b[1:3, ]) #슬라이싱
print(b[-1, ])
print(b[0, 0], b[1, 1])
print(b[[0]])

print()
c = np.zeros((2, 2)) #0으로 2행 2열을 채운다
print(c)

print()
d = np.ones((2, 2)) #1로 2행 2열을 채움
print(d)

print()
e = np.full((2, 2), fill_value = 7) #원하는 값으로 2행 2열을 채움
print(e)

print()
f = np.eye(2) #단위 행렬 생성
print(f)

#난수 생성
print()
print(np.random.rand(5), np.mean(np.random.rand(5))) #균등분포 음수 X
print(np.random.randn(5), np.mean(np.random.randn(5))) #정규분포 음수 O

print()
np.random.seed(1)
print(np.random.randn(2, 3))

print('--')
print(np.random.randint(10, size = 6)) #1차원
print('--')
print(np.random.randint(10, size = (3, 4))) #2차원
print('--')
print(np.random.randint(10, size = (3, 4, 5))) #3차원

print()
print(list(range(0, 10)))
print(np.arange(10)) #arange는 수열을 생성하는데 numpy에 있는 array를 생성할 때 사용

print('-------인덱싱과 슬라이싱-------')
a = np.array([1, 2, 3, 4, 5])
print(a[1:5:2])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[:])
print('--')
print(a[1:])
print('--')
print(a[-1:])
print('--')
print(a[0], a[0][0], a[[0]])
#1차원 반환, 스칼라 반환, 2차원 반환
print('--')
print(a[0], a[0][0], a[0, 0], a[[0]])
#a[0][0], a[0, 0] 둘은 같은 스칼라를 반환함
print('--')
print(a[1:,0:2])

print()
b = a[:2, 1:3] #서브배열 
print(b)
print(b[0,0]) #b는 a의 일부분만을 배열로 저장함
print(a[0,1])
print('--')
b[0, 0] = 88
print(b)
print()
print(a)

print()
c = a[:2, 1:3].copy() #배열 사본 복사
print(c)
c[0, 0] = 99
print()
print(c)
print()
print(a)

print("-----------")
a = np.array([[1, 2, 3], [4, 5, 6], (7, 8, 9)]) #tuple도 가능 {} set은 안 됨
print(a)
print()
print(a.shape)

print()
r1 = a[1, :]
print(r1)

print()
r2 = a[1:2, :]
print(r2)

print()
print(r1, r1.shape)
print()
print(r2, r2.shape)

print()
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a.shape)
print(a)

print()
b = np.array([0, 2, 0, 1]) #a배열 인덱싱용 배열로 1행 0열, 2행 2열, 3행 0열, 4행 1열이 b에 담김
print(b, b.shape)

print()
print(np.arange(4))
print(a[np.arange(4), b])

print()
bool_idx = (a > 10)
print(bool_idx)

print(a[bool_idx])
print(a[a > 10])


















