#함수 작성


a = 1
b = a + 1
#여러 동작들을 수행하다가 모듈의 멤버로 함수 선언

def DoFunc1(): #python에서 함수의 이름은 대문자나 소문자 내 마음 class는 대문자로 시작
    print("DoFunc1 수행") #함수를 만들면 객체가 만들어지고 함수의 이름은 객체의 주소를 가지고 있다
#함수는 반드시 작성 후 선언
c = b + 20

#다른 작업을 하다 함수 선언해보기
DoFunc1() #함수 호출

#다른 작업을 하다 함수가 필요할 때 다시 선언
res = DoFunc1()
print(res) #함수는 어떤 값을 반환하는데 return을 찍지 않으면 none이 반환됨
print(DoFunc1())
print(DoFunc1) # -> () 가 없으면 함수 호출 불가
print(id(DoFunc1)) #함수도 객체
print(id(print))
print(id(sum))
print(id(c))

DoFunc2 = DoFunc1 #DoFunc1 함수 객체의 주소를 치환
DoFunc1
DoFunc2()

print("-----------------")

def doFunc3(arg1, arg2): #함수() paraeter 가인수 매개변수
    res = arg1 + arg2
    #return res #return이 발생하면 밑에 if문은 수행 X
    if res % 2 == 1: #res값이 홀수면 return 값이 none
        return
    else: 
        return res

doFunc3(10, 20) #argument 실인수
#이렇게만 하면 출력이 안 됨 죽은 함수라고 함

print("결과는 ", doFunc3(10, 22)) #arg1과 arg2에 알아서 맷칭되는데 숫자 10과 20의 주소값을 가지고 있다 
aa = doFunc3(10, 20)
print("결과는 ",aa)

print("-----------------")

def area_tri(a, b):
    c = a * b / 2
    aria_print(c) #함수는 함수를 부를 수 있다
    
def aria_print(c):
    print("삼각형의 면적은 " + str(c))

area_tri(5, 6) #숫자 5와 6은 parameter a와 b에 맷칭됨

print("-----------------")

def func1():
    print("func1 멤버 처리")
    def func2(): #함수 안에 함수가 있을 수 있다
        print("func2 멤버 처리 : 내부 함수")
    func2()
func1()

print("-----------------")

def swap(a, b):
    return b,a #리턴되는 값은 tuple로 묶인 하나다 b,a 순서로 리턴되어 값의 순서가 바뀐다
a = 10; b = 20
c = swap(a,b)
print(c)
print(c[0], c[1])

print("-----------------")

#if 조건식 안에 함수를 사용하기

def isOdd_func(arg):
    return arg % 2 == 1

mydict = {x: x * x for x in range(11) if isOdd_func(x)} #if의 조건으로 함수가 들어갈 수 있다
print(mydict)

print("-----------------")

#print(dir(__builtins__)) #사용 가능한 모든 빌트인 함수가 나옴
print("현재 파일(모듈)의 객체 목록 : ", globals())



print("프로그램 종료")




    