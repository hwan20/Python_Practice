#메소드 오버라이드 : 다형성

class Parent:
    def printData(self): #다형성을 가지기 위해 자식들에게 override 시키기
        pass #상속받는 클래스에서 printData를 오버라이드해서 사용하게 하기

class Child1(Parent):
    def printData(self):
        print("Child에서 override")

class Child2(Parent):
    def printData(self):
        print("Child2에서 override")
        print("부모 메소드와 이름은 같으나 기능이 다름")
    
    def abc(self):
        print("Child2 고유 메소드")

c1 = Child1()
c1.printData()
print("-----------------")
c2 = Child2()
c2.printData() #같은 printData이지만 c1과 c2는 다름
c2.abc()

#다형성 때문에 override를 하는 것 다형성 다형성 다형성 다형성 다형성 다형성 다형성 

print("-----------------")
#par = Parent() #부모 객체 변수를 만들고  python에서는 이 부분 생략 가능
par = c1 #자식의 변수를 치환한다
par.printData() #자식의 객체를 받아서 c1의 printData를 받음
print("-----------------")
par = c2
par.printData() #c2의 객체를 받아서 c2의 printData를 받음
#par.printData() 는 c1과 같은 이름이나 하는 역할이 다름
par.abc() #overriding 하지 않아도 출력 가능

print("-----------------")
plist = [c1, c2]

for a in plist:
    a.printData() #이렇게도 나옴!!!!!!!!!! 12시 04분











