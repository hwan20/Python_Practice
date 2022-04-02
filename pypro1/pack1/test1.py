'''
여러 줄 주석
'''

"""
작은 따옴표나 큰 따옴표 3번이면
"""

#한 줄 주석 python은 작은 따옴표와 큰 따옴표를 구분하지 않는다
#print "aa" 이렇가 큰 따옴표로 작성되면 python version 2점대

print ("HelloWorld") #이렇게 함수식으로 선언
print ('HelloWorld"안녕하세요"') #;(세미클론)은 없어도 상관 X
print ("HelloWorld'안녕하세요'") #들여쓰기 하면 블록 안이라고 판단해서 에러남
a="안녕" #객체의 주소를 기억 참조형 기억 장소 
a='반가워'
print(a)
a=10; b=20.5 #이렇게 한 줄에 스테이트 먼트가 2가지 이상이면 세미클론 필수
print(a)
print(b)
c=b #객체의 주소 치환
print(a, b, c)
print(id(a), id(b), id(c)) #객체의 주소값 b와 c의 두 주소의 숫자가 같은 이유는 같은 주소값을 공유하기 때문

#Java는 동적(heap영역)이지만 python은 정적(static영역)이며 데이터 타입은 기본형이 없이 참조형밖에 없다
#들어오는 데이터 값에 따라 타입이 달라진다(object type)

a=10
b=10
print(a == b, a is b) # ==은 값 비교 연산자, is는 주소 비교 연산자 객체는 한 번만 만들어짐

aa=[10]
bb=[10]
print(aa == bb, aa is bb) #[]은 집단이라 주소값이 같지 않다

print()
A=1; a=2 #변수명은 대소문자를 구분 변수명은 숫자로 시작X 특수문자로 시작X 한글을 변수의 이름으로 사용하면 안 좋음 데이터로 사용 
print(A,a,id(A),id(a))

print()
import keyword
print('예약어 : ', keyword.kwlist) #정해진 예약어들을 변수 명으로 사용하면 안 됨

#python은 코드를 줄이려고 노력함
print("자료형 확인") #전부 class type 전부 object이다
print(3, type(3)) #정수면 무조건 int -> short, long 등이 없다
print(3.4, type(3.4)) #실수면 float
print(3+4j, type(3+4j)) #실수와 허수 복소수 complex
print(True, type(True)) #boolean 타입 bool
print("kbs", type("kbs")) #String 타입

#묶음형 python에는 배열이 X
print((1,), type((1,))) #()로 묶으면 tuple , 빼면 int
print([1], type([1])) # []로 묶으면 list 타입
print({1}, type({1})) # {}로 묶으면 set 타입
print({"key":1}, type({"key":1})) #key, value로 묶으면 dict 타입 json문자열과 같아 보임 python에서 json은 사용하지 않음











