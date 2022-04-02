#class : 메소드(함수)나 변수 등을 포함한 별도의 집합체(객체, 개체, Object) - 객체 중심의(지향적) 프로그래밍이 가능


class Car:
    handle = 0 #전역 변수
    speed = 0 #prototype이라고도 함 초기치

    def __init__(self,name,speed): #self는 반드시 있음
        self.name = name #지역 변수
        self.speed = speed #외부에서 받아온 speed의 값은 self.speed에 간다 
        #self.speed는 전역이 아니다, speed는 지역 ?? 확실치 않음
        #self는 car1의 객체 주소를 말하는데 __init__으로 받은 speed를 car1의 speed에 담는다는 뜻?
        #car1의 객체에 변수를 호출했는데 없을 때 Car 클래스에서 변수를 찾아 값을 리턴시켜줌 -> 이건 맞음
        
    def showData(self):
        km = "킬로미터" #showData의 지역변수
        msg = "속도 : " + str(self.speed) + km + "확인한 사람 : " + self.name
        return msg


print(Car.handle) #원형 클래스의 멤버 - handle 필드의 값. prototype 값 출력
car1 = Car("tom", 10) #클래스의 이름을 선언해서 넣어줌
print(car1.handle, car1.name, car1.speed) #car1에는 handle이 없어 오리지널 객체에 들어가서 찾아옴
#java와 python의 핵심은 같은데 표현 방법이 다름
#객체가 새로 생성될때 함수 멤버는 같이 복사가 되는데 field는 복사가 안 되나?

car1.color = "검정" #이 순간 car1 객체에 color라는 메소드가 생기고 "검정"이라는 값이 들어간다
print(car1.color)

print()
car2 = Car("james", 20) #새로운 객체가 생성됨
print(car2.handle, car2.name, car2.speed)
#print(car2.color) car2에는 color가 없음

print()
print(car1.showData())

print("---------------------")
ss = car2.showData() #이렇게 변수에 car2.showData()의 주소값을 변수에 치환하는 것도 가능하다
print(ss)

print()
print("주소 : ", id(Car), id(car1), id(car2)) #Car와 Car를 생성한 객체의 주소 값이 다 다름

print()
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)

car1.speed = 80
print(car1.showData())
print(car2.showData())

Car.handle = "한 개" #Car 객체의 변수 값이 바뀌면 생성된 객체들의 변수 값도 바뀐다. -> 해당 메소드에 같은 이름을 가진 지역 변수가 없을 때만
print(Car.handle)
print(car1.handle)
print(car2.handle)

print()
car3 = Car(15,"choi") #순서대로 들어간다
print(car3.__dict__)



