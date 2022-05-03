#최소 제곱해를 선형 행렬 방정식으로 얻기
#주요 사항
# - 독립 변수와 종속 변수 사이에는 선형 관계가 있어야 한다.
# - 복수 독립 변수의 경우, 중요한 독립 변수를 선택하는 것이 중요하다. 

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.5, 2.1])

#plt.plot(x, y, 'o', label='Original data', markersize=10)
#plt.legend()
#plt.grid()
#plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A) #1차원 벡터가 4행 2열 2차원 매트릭스가 됨

import numpy.linalg
w, b = np.linalg.lstsq(A, y)[0] #최소 자승법 linalg.lstsq을 사용(내부적으로 편미분 사용)
print('w : ', w, ', b : ', b) #기울기w :  0.9599999999999999 , 절편b :  -0.9899999999999993

#단순선형회귀식이 만들어짐 y = (0.9599999999999999* x) + (-0.9899999999999993)
print("y예측값1 : ", (0.9599999999999999* 0) + (-0.9899999999999993)) #x가 0일 때 y=-0.9899999999999993
print("y예측값2 : ", (0.9599999999999999* 1) + (-0.9899999999999993)) #x가 1일 때 y=-0.02999999999999947
print("y예측값3 : ", (0.9599999999999999* 2) + (-0.9899999999999993)) #x가 2일 때 y=0.9300000000000004
print("y예측값4 : ", (0.9599999999999999* 3) + (-0.9899999999999993)) #x가 3일 때 y=1.8900000000000001

#x가 특정 값일 때 미지의y예측값
print("미지의 y예측값 : ", (0.9599999999999999* 10) + (-0.9899999999999993)) #x가 10일 때의 미지의 y예측값

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, w*x + b, 'r', label='Fitted line')
plt.grid()
plt.legend()
plt.show()





