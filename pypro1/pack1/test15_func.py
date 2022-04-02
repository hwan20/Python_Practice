#closure : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다.
#내부 함수의 멤버를 함수 밖에서 참조가 가능 내부 함수의 주소를 반환해 사용한다



def funcTimes(a, b):
    c = a * b
    return c

print(funcTimes(2,3))

kbs = funcTimes(2,3) #함수의 실행 결과를 리턴함 실행 결과를 치환
print(kbs)

kbs = funcTimes #함수의 주소를 가져옴
print(kbs)
print(kbs(2,3)) #kbs와 funcTime는 완전 똑같다 주소를 치환한 개념
print(id(kbs), id(funcTimes)) #같은 객체를 참조하고 있어 id의 주소가 같음

del funcTimes #함수를 지움
#print(funcTimes(2, 3)) #funcTime 함수를 삭제해서 돌아가지 않는 코드
print(kbs(2,3)) #본래 함수가 삭제가 되어도 함수의 주소를 받은 kbs는 사용 가능

mbc=sbs=kbs #이렇게 함수의 주소 값을 치환하여 여러 곳에서 사용 가능
print(mbc(2,3)) 
print(sbs(2,3))

print("------클로저를 사용하지 않는 경우------")

def out():
    count = 0
    def inn():
        nonlocal count #out 함수의 카운트를 사용하기 위해 count가 지역 변수가 아니라고 선언함
        count +=1
        return count
    print(inn()) #이 부분이 다름
    
out()
out() #count는 계속 늘어나고 있지만 out 함수의 값은 여전히 1이다
#print(count) 함수 안에 있는 명이라 호출이 안 됨

print("------클로저를 사용하는 경우------")
#중첩 함수를 사용할 때 내부의 주소를 반환하기 위해 사용
def outer():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner    # 이거를 클로저라고 부른다. 내부함수의 주소를 반환 함수

var1 = outer() #outer() 함수를 실행해서 inner()의 주소를 치환함 
print(var1)
print(var1())
print(var1()) #내부 함수의 주소를 받았기 때문에 함수 밖에서도 내부 함수를 실행 가능
imsi = var1()
print(imsi)
print()
var2 = outer() #객체를 새로 생성해서 값이 1로 다시 돌아감
print(var2())
print(var2())
#Car car1 = new Car 와 Car car2 = new Car 했을 때 car1와 car2의 객체가 다른 것처럼
print(id(var1), id(var2), type(var1), type(var2)) #outer함수의 리턴된 값을 치환받아 둘 다 주소가 다르다
var3=outer
var4=outer
print(id(var3),id(var4)) #주소를 치환 받으면 주소가 같다
print("수량 * 단가 * 세금을 출력하는 함수")

def outer2(tax): #tax는 지역 변수이다 함수 내에서만 사용 가능
    def inner2(su,dan):
        amount = su * dan * tax
        return amount
    return inner2 # 내부 함수를 리턴하는 것이 클로저 이렇게 해야 내부 함수의 값을 리턴받아 다른 곳에서 사용 가능

#1분기에는 수량 * 단가에 대해 tax가 0.1이 부과
q1 = outer2(0.1) #outer 함수의 tax에 0.1을 부과하는 것
result1 = q1(5, 50000) #q1에는 outer2의 return 값인 inner2의 주소를 가지고 있다 inner2의 파라미터에 5와 50000이 맵핑됨
print("result1 : ", result1)
result2 = q1(2, 10000)
print("result2 : ", result2)
print("--------------------------------")
q2 = outer2(0.05)
result3 = q2(5, 50000)
print("result3 : ", result3)
result4 = q2(2, 10000)
print("result4 : ", result4)

#함수 내부에 있는 함수를 외부 함수에서 리턴시켜서 함수 외부에서 내부 함수 안에 있는 파라미터와 return 값들을 사용할 수가 있다



