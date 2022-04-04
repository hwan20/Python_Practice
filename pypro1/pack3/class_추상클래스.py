#추상 클래스 : 추상 메소드를 하나라도 가지고 있는 경우 대체적으로 추상 클래스라고 한다
#추상 클래스를 사용하는 이유 - 클래스를 상속받는 클래스가 overriding을 필수적으로 사용하게 하려고(다형성을 목적으로)
#overriding하지 않으면 객체 생성이 안 됨

from abc import *   #metaclass = ABCMeta 가독성이 좋은 것 외에도 없으면 에러가 생김
class AbstractClass(metaclass = ABCMeta): #이게 추상 클래스
    
    @abstractmethod #추상 메소드를 만들기 위해서 항상 있어야함 무조건 오버라이딩 필수
    def abcMethod(self): #해당 클래스를 상속받는 클래스는 이 메소드를 반드시 overrding해야함
        pass
    
    def normalMethod(self): #일반 메소드 오버라이딩 하든가 말든가
        print("추상 클래스 내의 일반 메소드")

#일반 클래스라면 에러가 안 생기는데 추상 클래스라서 에러가 생김
#aa = AbstractClass() #TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod

class Child1(AbstractClass): #괄호에 아무것도 없으면 에러가 X 괄호에 추상 클래스를 상속받는 순간 특정한 조건을 이루어야 객체를 생성할 수가 있음
    name = "난 Child1"
    
                        #추상 클래스의 파생 클래스는 반드시 추상 메소드를 overriding 해야 한다. 강제
    def abcMethod(self): #추상 클래스 AbstractClass의 추상 메소드를 overriding해서 이제 사용 가능
        print("추상 메소드를 오버라이딩")
    
c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print("------------------------")
class Child2(AbstractClass):
    a=10
    b=20
    
    def abcMethod(self): #overriding을 강요당함
        print("추상 메소드2, 오버라이딩 해서 족쇄에서 풀림")
    
    def normalMethod(self): #얘는 일반 메소드 overriding이 선택적
        print("부모 클래스의 메소드를 다시 정의함")


c2 = Child2()
print(c2.a, c2.b)
c2.abcMethod()
c2.normalMethod()

print("--------다형성--------")
#이름은 같지만 내용이 다름 이게 다형성
mbc = c1
mbc.abcMethod()
print()
mbc = c2
mbc.abcMethod()


















