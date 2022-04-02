#Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리한다.
#파이썬은 모듈 단위의 파일로 저장된다.
#모듈의 멤버 : 변수, 실행문, 함수, 클래스
#모듈을 사용하려면 import해야함
#main Module 확인 : __name__=="__main__" 이 조건을 만족하면 main module 이다

#내장된 모듈 Standard Module

print("어떤 작업을 하다가~~") #print도 자동으로 import되어있는 기본 module이다

import sys
print(sys.path)
#sys.exit() #프로그램 강제 종료

import math #numpy가 대부분 가지고 있음 데이터 분석의 대부분은 numpy기반
print(math.pi)
print(math.sin(math.radians(30))) 

import calendar
calendar.setfirstweekday(6) # 요일은 7일 0~6 이걸 안 주면 월요일이 제일 먼저 나옴
calendar.prmonth(2022, 3) # 2022년 3월 달력이 나옴

print(dir(calendar))

import time
print(time.localtime())
print("start...")
#time.sleep(3) #지연 시간을 주는 것 java에서는 thread
print("finish")

import os
print(os.getcwd()) #현재 작업 경로

import random
print(random.random())
print(random.randint(1, 10))

from random import randint #자주 언급될 경우 이렇게 사용
print(randint(1, 10))

#from random import * #사용은 가능하지만 메모리 소모가 심해서 좋지 않다
#print(random())


print("프로그램 종료")





