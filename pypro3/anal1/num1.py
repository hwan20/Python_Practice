#numpy : 고속연산, ndarray를 지원
#데이터 분석 관련 모듈 전체 생태계의 핵심을 이루고 있기에 잘 다를 줄 알아야 한다.

#평균, 분산, 표준편차 구하기(모집단 / 표본 통계량)


grades = [1, 3, -2, 4] #입력값 1, 3, -2, 4가 있다고 하자 이것은 변량(변수, 확률값, 관측값)이라고 하고 숫자로 나타낼 수 있는 자료들이다
#변량 x에 대해서 평균 x바를 구할 수 있다(x-x바(평균)) 편차 편차에서 variance가 나온다?
#(x-x바(평균))의 합은 0이니 제곱을 씌어줌. -> 음수도 양수로 바꿔줌
#(x-x의 평균)^2의 합을 n으로 나눔 -> 편차 제곱의 평균 variance
#편차 제곱의 평균은 실제 편차보다 크기가 크다. 제곱을 씌어줬으니
#그래서 편차 제곱의 평균을 루트를 씌어줌 -> 이 값을 표준 편차라고 하고 시그마라고 부른다
#R은 자유도를 사용하므로 n-1로 나눔 표본 집단을 사용,  파이썬은 n만 씀 모집단을 사용


def show_grades(grades):
    for g in grades:
        print(g, end = ' ')

show_grades(grades)

def grades_sum(grades):
    tot = 0
    for g in grades:
        tot += g
    return tot

print()
print("grades의 합 : ", grades_sum(grades))

def grades_avg(grades):
    tot = grades_sum(grades)
    ave = tot / len(grades)
    return ave

print("grades의 평균 : ", grades_avg(grades))

def grades_varience(grades):
    ave = grades_avg(grades)
    vari = 0
    for su in grades:
        #vari += (su) #변량
        #vari += (su - ave) #편차 =  변량에서 평균을 뺌
        vari += (su - ave) ** 2 #편차 제곱의 합을 구함
        
    return vari / len(grades) #모집단으로 계산한 것(python) 편차 제곱의 평균 variance
    #return vari / (len(grades) - 1) #표본 집단으로 계산(R) 샘플데이터  len(grades)의 값이 크면 자유도 -1을 줘도 값이 비슷
#분산도가 크다 -> 데이터가 흩어져있다 -> 산포도가 크다 -> 상관계수는 0에 가까움
#분산도가 작다 -> 데이터가 모여있다 -> 산포도가 작다 -> 상관계수는 1에 가깝다
#그러나 현재는 독립변수가 하나이니(grades) 상관계수가 나오지 않음

print("grades의 분산 : ", grades_varience(grades))

import math
def grades_std(grades):
    #return grades_varience(grades) ** 0.5 #제곱한 것을 풀어줌 - 평균값과 얼마나 차이가 나는 지를 분산가지고 알아낼 수가 있지만 분산값은 제곱을 했기 때문에 크다   
    return math.sqrt(grades_varience(grades)) #위와 같음

print("grades의 표준 편차 : ", grades_std(grades)) #R과는 답이 다름, 표준 편차에서 -1을 안 했기 때문


print("numpy로 계산")
import numpy as np
#print("numpy로 구한 grades의 합은 : ", numpy.sum(grades))
print("numpy로 구한 grades의 합 : ", np.sum(grades))
print("numpy로 구한 grades의 평균 : ", np.average(grades)) #일반적인 평균
print("numpy로 구한 grades의 평균 : ", np.mean(grades)) #중간 값을 가지는 항은 mean을 사용
print("numpy로 구한 grades의 분산 : ", np.var(grades))
print("numpy로 구한 grades의 표준편차 : ", np.std(grades))

#numpy는 여러 함수들을 지원한다
#이러한 함수들은 pandas나 TensorFlow에서도 그대로 쓰인다
#데이터 분석 관련 모듈들은 numpy를 기본으로 하기 때문이다 
















