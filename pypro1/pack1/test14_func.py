#함수 : 실인수(매개변수)와 가인수의 매핑
#매개변수의 유형
#위치 매개변수, 기본값 매개변수(입력값이 없으면 default 값을 사용), 키워드 매개변수(이름에 의한 매핑), 가변 매개변수

def showGugu(start, end = 5):
    for dan in range(start, end +1):
        print(str(dan)+"단 출력")

showGugu(2,3) #위치 매개변수
print()
showGugu(3) #start의 값만 줌
print()
showGugu(start=2,end=3) #키워드 매개변수
showGugu(end=3,start=2) #키워드로 매핑하는 거라 순서 상관 X
print()
showGugu(2, end = 3) #위치와 키워드 매핑
print()
#showGugu(start=2, 3) #err 
#showGugu(end=3, 2) #첫 번째 인자가 아닌 곳에 상수값을 줘 버리면 에러가 난다

print()
def func1(*ar): #패킹 연산자인 *을 사용하면 갯수를 여러 가지 받을 수가 있다
    print(ar)

func1("김밥")
func1("김밥", "비빔밥")
func1("김밥", "비빔밥", "볶음밥")

print()

#def func2(*a, ar): #앞에 패킹 연산자가 붙으면 *a이 모든 요소들을 다 가져가 ar이 값을 가져갈 수가 없다
def func2(a, *ar): #패킹 연산자인 *을 사용하면 갯수를 여러 가지 받을 수가 있다
    print(a) #김밥은 a가 가져가서 앞에 배고프면 이라는 단어가 안 붙는다
    for i in ar: #2,3번 인자를 가져가 음식 이름 앞에 배고프면을 붙인다
        print("배고프면 ", i)

func2("김밥")
func2("김밥", "비빔밥")
func2("김밥", "비빔밥", "볶음밥")

print()
def process(choice, *ar): #process에서 첫 번째 글자만 choice에 담고 나머지 숫자들은 *ar에 담는다
    if choice == "sum" :
        res = 0 #더하기를 누적시킬 변수에 초기값 0을 준다
        for i in ar: #ar의 요소들을 i에 주고 요소들만큼 반복시킨다
            res += i
    elif choice == "mul":
        res = 1 #곱하기를 시킬 건데 초기값이 0이면 0이 나오니 1을 준다
        for i in ar:
            res *= i
    return res #choice의 값에 따라 나온 값을 return 시킨다
        
        
print(process("sum", 1, 2, 3, 4, 5))
print(process("mul", 1, 2, 3, 4, 5))
print(process("mul", 1, 2, 3))

print()
def func3(w, h, **other):
    print("몸무게 : {}, 키 : {}".format(w,h))
    print(other)


func3(66, 177)
print()
func3(66, 177, irum="지구인", nai = 22) #처음부터 dict를 주면(key,value를 주면) 안 됨 다른 값을 먼저 넣고 밀어넣어야 함
func3(66, 177, irum="한국인")

print()
def func4(a, b, *v1, **v2):
    print(a,b)
    print(v1)
    print(v2)
    
func4(1, 2)
func4(1, 2, 3, 4, 5, 6, 7)
func4(1, 2, 3, 4, 5, m=6, n=7)







