#일급 함수 지원 성립 조건
#1. 함수 안에 함수를 선언할 수 있어야 함
#2. 인자로 함수를 전달할 수가 있어야 함
#3. 반환 값이 함수인 경우
#이 3가지 조건을 만족할 수 있으면 1급 함수다

def func1(a,b):
    return a+b

func2 = func1 #내부에 리턴되는 값을 전달하는 게 아니라 func1의 주소를 치환함 그래서 주소 값이 같음
print(func1(2,3))
print(id(func1))
print(func2(2,3))
print(id(func2))

print()
def func3(f):                   #2. 매개 변수로 함수를 사용
    def func4():                #1. 함수 안에 함수를 선언
        print("나는 내부 함수야~")
    func4()
    return f  #반환 값이 fun1이다  #3. 반환 값이 함수이다. 3가지 경우를 모두 충족
            #func3은 func1을 받는다
mbc = func3(func1) #func1을 func3의 인자에 줌 func3의 인자 f에 fun1의 주소가 넘어감
print(mbc(2,3))
print(id(mbc))

print("----------람다(lambda)함수, 축약 함수 : 이름이 없는 한 줄 짜리 함수----------")
#람다 함수는 def를 쓸 정도로 복잡하지 않거나, def를 쓸 수 없는 곳에 사용된다
#java는 람다를 쓰기에 구조적으로 좋지가 않다
#형식 : lambda 인자 : 표현식 -> 인자에 여러 인자를 줄 수 있다 return 없이 결과를 반환한다

def Hap(x,y):
    return x+y

print(Hap(2,3)) #일반 함수 인자에 값을 전달하고 리턴값을 받아오는 방식

print((lambda x, y : x + y)(1,2)) #이렇게 하면 1회용 lambda 함수

#이름이 없는 한 줄 짜리 lambda 함수를 변수에 담아서 다회성으로 사용할 수 있다
g = lambda x, y : x * y #하지만 대체적으로 1회용 함수로 사용된다 아규먼트 없이 표현식만 사용할 수도 있다
print(g(3, 4))
imsi = g(3, 4)
print(imsi)

print()
kbs = lambda a, su=10 : a+su #람다도 가변 인자를 사용할 수 있다
print(kbs(5))
print(kbs(5,6)) #su=10에 6을 덮어 씌어서 값은 11이 나온다

sbs = lambda a, *t, **di : print(a, t, di) #패킹 연산자도 같이 사용이 된다
sbs(1, 2,  3, m=4, n=5)

print()

li = [lambda a, b : a + b, lambda a, b : a * b]
print(li[0](3,4)) #인덱싱으로 인자에 값을 전달되는 것도 가능
print(li[1](3,4))

print()

#filter(함수, sequence자료) sequence자료에서 함수에 해당하는 것만 걸러서 보겠다
print(list(filter(lambda a:a<5, range(10)))) #이렇게 작은 함수는 lambda 함수를 사용한다. 따로 함수를 만들어서 사용도 가능
print(list(filter(lambda a:a%2, range(10)))) #0~9를 2로 나누면 0이나 1이 나오는데 0이면 false 1이면 true이니 홀수만 출력
print(list(filter(lambda a:a%5==0 or a%7==0, range(1,101))))

















