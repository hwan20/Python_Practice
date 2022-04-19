#배열 연산 

import numpy as np

x = np.array([[1, 2], [3, 4]], dtype = np.float64) #정수를 실수 타입으로 만들고 싶을 때 데이터 타입을 정해줄 수가 있다
print(x, x.dtype)

print()
#y = np.arange(5, 9) 
y = np.arange(5, 9).reshape((2, 2)) #1차원 5,6,7,8을 2차원으로 바꿈
y = y.astype(np.float64) #데이터 타입을 바꾸고 싶으면
print(y, y.dtype)

print()
print(x + y) #각각의 열을 더함
print(np.add(x, y)) #내장함수 

print()
print(x - y)
print(np.subtract(x, y))

print()
print(x * y)
print(np.multiply(x, y))

print()
print(x / y)
print(np.divide(x,y))

print()
v = np.array([9, 10])
w = np.array([11, 12])
print(v * w) #[ 99 120] 차원이 줄어듦

print('============================')
print(v.dot(w)) #219 백터 내적 연산 v[0] * w[0] + v[1] * w[1]
print(np.dot(v, w)) #scalar

print(x.dot(v)) # x[0,0] * v[0] + [0,1] * v[1]     x[1,0] * v[0] + x[1,1] *v[1]
print(np.dot(x, v))

print(x.dot(y)) #한 번 구해보기
print(np.dot(x, y))

#1차원끼리 곱하면 scalar가 나오고 1차원 2차원을 곱하면 vector, 2차원끼리 곱하면 2차원으로 나옴

print()
print(x)
print()
print(np.sum(x))
print()
print(np.sum(x, axis = 0)) #열에 대한 합
print()
print(np.sum(x, axis = 1)) #행에 대한 합

print()
print(x)
print(np.argmax(x), np.argmin(x)) #최대 최소값의 인덱스를 리턴

print()
print(x)
print(x.T) #전치
print(x.transpose()) #전치
print(x.swapaxes(0, 1)) #전치

print()
#Broadcasting 연산 : 크기가 다른 배열간 연산을 하면 작은 배열이 큰 배열의 크기에 자동으로 맞춰져 연산한다
x = np.arange(1, 10).reshape(3, 3)
print(x)
y = np.array([1, 2, 3])
print(x + y)


#file io
datas = np.arange(0, 10, 2)
print(datas)
#만약 가공이 끝난 데이터라고 가정. 파일로 저장하기
np.save("test1", datas) #확장자는 자동으로 지정됨    binary형식으로 저장. 확장자는 npy
np.savetxt("test2.txt", datas) #실수형으로 저장됨

print()
mydatas = np.loadtxt("test2.txt")
print(mydatas) #실수 타입으로 저장되어 부를 때도 실수 타입으로 불러짐














