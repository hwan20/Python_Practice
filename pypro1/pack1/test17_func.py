#함수 장식자 (function decorator) : meta 기능이 있다
#함수 장식자는 또 다른 함수를 감싼다

def make2(fn):
    return lambda : "안녕 " + fn() #lambda가 리턴된다

def make1(fn):
    return lambda : "반가워 " + fn()

def hello():
    return "홍길동"

hi = make2(make1(hello)) #make1의 return 되는 주소가 make2의 fn에 들어감 make2의 리턴되는 주소는 hello 함수 이다
print(hi())
print(id(hi))

print()

@make2 #mak2는 mak1을 포함하니 이렇게 작성
@make1 #make1은 hello2를 포함하고
def hello2():
    return "고길동"

print(hello2())

print()

hi2=hello2() #이건 hello2의 실행 결과를 치환
print(hi2)

hi3=hello2 #이건 hello2의 주소를 치환
print(hi3()) #주소를 치환해서 호출하기 위해서는 ()를 해줘야 한다

















