#function : 자원의 재활용 가능, 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위이다.
#내장 함수 : 프로그램을 만든 사람이 제공하는 함수
#사용자 정의 함수 형식 : def 함수명(parameter) : 내용~
print("표준 출력 장치로 데이터를 출력하는 내장 함수")
print(sum([3,5,7]))
print(bin(8)) # 2진수
print(int(1.7), float(2), str(5)+"5")
a = 10
b = eval("a+5") #수식의 모양을 하고 있는 데이터를 계산해주는 명령어
print(b)

print(all([True, False])) #모두가 True어야 True
print(any([True, False])) #하나라도 True면 True
a = [1, 3, 2, 5, 7, 6, 11]
res = all(i < 10 for i in a)
print("모든 숫자가 10 미만이면 출력",res)

print()
x = [1, 2,  3]; y = ["a", "b"] 
for i in zip(x, y): #인덱스 별로 짝을 지어줌 짝이 없으면 출력하지 않는다
    print(i) #tuple로 출력

print(round(1.2), round(1.6)) #근사치의 정수로 반올림

import math #ceil이나 floor은 외부 함수이기 때문에 import해야 한다
print(math.ceil(1.2), math.ceil(1.6)) #정수로 올림해버린다
print(math.floor(1.2), math.floor(1.6)) #내림해버린다
print(math.pi) #값을 가지고 있는 field






















