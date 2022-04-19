#numpy

import numpy as np

aa = np.eye(3)
print(aa)

print()
bb = np.c_[aa, aa[2]] #2열과 동일안 열 추가
print(bb)

print()
bb = np.c_[aa, aa[2]] #2열과 동일안 열 추가
print(bb)

print()
cc = np.r_[aa, [aa[2]]] #행 추가
print(cc)

print("----------append, insert, delete----------")

a = [1, 2, 3] #1차원
b = np.append(a, [4, 5]) 
print(b)

print()
c = np.insert(a, 0, [6, 7]) #0은 인덱스 나머지 뒤로 밀림
print(c)

print()
d = np.delete(a, 1) #1번째 인덱스 삭제
print(d)

print()
aa = np.arange(1, 10).reshape(3, 3)
print(aa)
print("--")
bb = np.arange(10, 19).reshape(3, 3) #2차원
print(bb)

print()
cc = np.append(aa, bb) 
print(cc) #[10 11 12 13 14 15 16 17 18  1  2  3  4  5  6  7  8  9]

cc = np.append(aa, bb, axis = 0) #행방향으로 벡터 추가
print(cc)
cc = np.append(aa, bb, axis = 1) #열방향으로 벡터 추가
print(cc)

print()
print(np.delete(aa, 1)) #[1 3 4 5 6 7 8 9]
print(np.delete(aa, 1, axis = 0)) #행기준
print(np.delete(aa, 1, axis = 1)) #열기준

print("------조건연산 where(조건, 참, 거짓)------")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
condData = np.array([True, False, True])
result = np.where(condData, x, y)
print(result)

print()
aa = np.where(x >= 2)
print(x[aa])

print()
kbs = np.concatenate([x, y]) #배열 결합
print(kbs)

print()
v1, v2 = np.split(kbs, 2) #배열 분할
print(v1)
print(v2)

print('--')
a = np.arange(1, 17).reshape(4, 4)
print(a)
x1, x2 = np.hsplit(a, 2)
print(x1)
print(x2)

print()
print(a)
x1, x2 = np.vsplit(a, 2)
print(x1)
print(x2)
print()

#복원 / 비복원 추출 기본이 비복원
li = np.array([1, 2, 3, 4, 5, 6, 7])

#복원 추출
for _ in range(5):
    print(li[np.random.randint(0, len(li) - 1)], end = ' ')

print()

#비복원 추출
import random
print(random.sample(list(li), k = 5))

print(random.sample(range(1, 46), k = 6))

print()
print(list(np.random.choice(range(1, 46), 6))) #비복원    [28, 24, 37, 42, 42, 10] ??
print(list(np.random.choice(range(1, 46), 6, replace = True))) #복원    [3, 37, 10, 3, 5, 31]

print()
arr = 'air book cat d e f god'
arr = arr.split(' ')
print(arr)
print(np.random.choice(arr, 3, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4 ])) 
#arr에 있는 문자열을 ' '를 기준으로 인덱싱하여 리스트 형식으로 저장한 후
#split한 문자열을 3개씩 출력하며, 각각 맞는 인덱스에 출력되는 확률을 부여한다 0.1 = 10%, 0.4 = 40% 







