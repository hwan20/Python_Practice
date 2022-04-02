#module 클래스
#클래스 : 클래스가 있어야 객체 지향적 언어를 사용 가능 OOP(객체 지향 프로그래밍) - 자원의 재활용을 목표로 함 (포함, 상속이 있으며 상속으로 다형성을 구사)
#클래스는 새로운 타입을 생성. 멤버 : 멤버 변수(필드), 멤버 메소드 생성자나 소멸자는 메소드의 일종. 접근 지정자 X Overloading X
#new를 쓰지 않는다. 클래스 선언 후 실행하면 객체가 생성된다.(prototype)

print(type(1))
print(type([]))

a= 1

def func():
    pass

"""
class asd:
    pass 이것도 클래스
"""

class TestClass: #new를 필요하지 않는다
    #pass
    aa = 1 #멤버 변수(필드)
                        #init이란 이름은 파이썬 내부에서 정해주는 이름
    def __init__(self): #__init__ 생성자 생성자의 내용이 없으면 적지 않아도 됨, 매개변수로 self라는 변수를 무조건 가지고 있음
        print("생성자 : 객체 생성시 초기화를 담당 초기에만 1회 부름 ")
        
        #callback 수행이 되면 자동으로 선언됨
    def __del__(self): #java에는 소멸자가 없다 보통은 사용하지 않지만 필요하면 garbage collector를 사용하면 된다
        print("소멸자 : 마무리를 담당") #python은 동적으로 동작해서 한 번 이상 필요하지 않는 클래스는 메모리에서 삭제하는 게 좋음 그때 필요한게 __del__
    
    def myMethod(self):
        name="신기해" #name 변수는 myMethod에 있는 지역 변수이다.
        print("클래스 내에 있는 함수를 메소드 : 반드시 self를 매개변수로 갖는다")
        print(name)
        print(self.aa) #클래서 내의 변수를 지적하고 싶으면 self.해야한다 그냥 

#이렇게는 잘 사용하지 않음
print(TestClass.aa, id(TestClass)) #클래스의 이름도 객체의 주소를 가지고 있다 클래스의 이름으로 .aa를 부르는 것임
#TestClass.myMethod() #이건 self를 못 줘서 에러가 남
print("--------------------------------")
#객체가 두 개가 생성이 됨 test와 TestClass
test = TestClass() #생성자를 호출하고 TestClass type의 객체가 생성됨 test가 TestClass의 주소를 가져감
print(test.aa)
test.myMethod() # Bound method call 자동으로 self를 자동으로 전달이 됨
TestClass.myMethod(test) #unBound method call 이렇게 부르고 싶으면 괄호에 test를 넣어야 함. 주소값을 넣어야 하나 봄
#TestClass.myMethod() #이건 self를 못 줘서 에러가 남. 명시적으로 객체 변수를 선언해줘야함
print("--------------------------------")
print()
print(type(test)) #우리가 만든 TestClass class type
print(isinstance(test, TestClass)) #test는 TestClass type이 맞으면 T가 리턴
print(id(test), id(TestClass)) #두 개의 객체 주소가 다름 두 개의 객체 생성






