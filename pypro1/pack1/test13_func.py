#변수의 생존 범위 (scope rule) : 전역 변수와 지역 변수
#접근 우선순서 Local > Enclosing function(내부함수 안에) > Global

player = "전국대표" #전역 변수 : 현재 모듈의 어디서든 공유가 가능

print(player)
def funcSoccer():
    name = "신선해" #지역 변수 : 현재 함수 내에서만 유효하다
    player = "지역대표"
    print(name, player) #글로벌 변수 plyer의 값은 다르지만 지역 변수라 우선 순위가 더 높은 지역대표로 바뀜

funcSoccer()
#print(name) NameError: name 'name' is not defined #지역 변수는 함수 내에서만 유효
print(player)

print("------------------------------")
a = 10; b = 20; c = 30
print("1) a:{} b:{} c:{}".format(a,b,c))

def foo():
    a = 40
    b = 50
    def bar():
        #c = 60 # 선언은 호출하기 전에 사용되어야 함
        global c #지역변수 c는 global 명령어 때문에 전역 변수로 바뀜 변수의 수준이 달라짐 기억해둬야 함
        nonlocal b #foo 함수 수준의 변수 b로 바뀜 잘 사용 안 함
        print("2) a:{} b:{} c:{}".format(a,b,c)) #a,b는 함수 foo의 지역 변수이고 c는 전역 변수이다
        c = 60 #UnboundLocalError: local variable 'c' referenced before assignment
        #print 2)의 c에 값이 바인드 되지 않아 에러가 생김 그 어떤 곳도 c를 사용하지 않았기 때문에 에러가 생김
        #위에 global c로 글로벌 변수로 선언했기 때문에 에러가 안 생김
        b = 70
    bar()
    print("3) a:{} b:{} c:{}".format(a,b,c))

foo()
print("처리 후 a:{} b:{} c:{}".format(a,b,c))

print("------------------------------")
g = 1
def func():
    global g #g를 a에 치환하고 g에 2를 치환하면서붙터 g는 지역변수가 됨 이 지역 변수가 사용될 곳이 없어 에러가 남 이때 global을 사용하면 에러가 안 남
    a = g # global g가 없다면 g에는 아무 값도 없어 a에 치환할 때 에러가 생기는 것
    g = 2
    return [a,g]

print(func())
print(g) #func 함수 안에서 g의 값을 바꾼게 함수 밖에서도 그대로 유지됨 global 명령어 때문에

















