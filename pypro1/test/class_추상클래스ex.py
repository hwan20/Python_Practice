#추상 클래스 연습문제

#추상 클래스는 추상 메소드를 가지고 있다.  
from abc import *
class Employee(metaclass = ABCMeta):
    
    def __init__(self,irum,nai): #irum, nai 변수는 필드로 줘도 되고 생성자로 하여 입력 받아도 된다
        self.irum = irum
        self.nai = nai
        #self는 생성되는 객체의 변수 주소이다
        
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print("이름 : " + self.irum + ", 나이 : " + str(self.nai), end = " ")
    
class Temporary(Employee):
    
    def __init__(self, irum, nai, ilsu, ildang):
        #irum과 nai는 부모에서 주고 있음. 부모에서 가져오면 됨
        #self는 생성된 Temporary객체를 가르킨다
        #생성되는 변수 irum, nai는 부모 클래스에 주고 ilsu, ildang은 자신이 가지고 있는다
        #하지만 Temporary 객체 안에는 4가지 변수가 다 있다
        Employee.__init__(self, irum, nai) # 생성된 Temporary 객체에 생성자로 irum과 nai를 넣음
        self.ilsu = ilsu
        self.ildang = ildang

    #추상 클래스의 추상 메소드는 overriding하지 않으면 객체가 생성되지 않는다    
    def pay(self):
        return self.ilsu * self.ildang
    
    def data_print(self): #t.data_print를 찍으면 출력하게 하기 위해
        self.irumnai_print()
        print(", 월급 : " + str(self.pay()))


t = Temporary("홍길동", 25, 20, 15000)
t.data_print()

class Regular(Employee):
    
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai) #super().으로 부모 클래스의 메소드를 불러올 수가 있다
        #super().__init__, Employee.__init__ 같이 부모 클래스를 부르는 말임
        self.salary = salary
    
    def pay(self):
        return self.salary

    def data_print(self): #부모 class의 irumnai_print()로 출력을 함
        self.irumnai_print()
        print(", 급여 : " + str(self.pay()))

r = Regular("한국인", 27, 3500000)
r.data_print()

class Salesman(Regular):
    
    def __init__(self, irum, nai, salary, sales, commission):
        #부모 클래스인 Regular에게 전달해주고 다시 Employee 클래스에 전달한다.
        #10시 10분 설명~~
        super().__init__(irum, nai, salary) 
        self.sales = sales
        self.commission = commission

    def pay(self):
        #부모가 가지고 있는 salary를 그대로 사용
        #성격이 다르면 유닛을 만들어라
        #프로그램을 단위적으로 만들기
        return self.salary + (self.sales * self.commission)
                #super().pay()
    def data_print(self): #부모 class의 irumnai_print()로 출력을 함
        self.irumnai_print()
        print(", 수령액 : " + str(self.pay()))

s = Salesman("손오공", 29, 1200000, 5000000, 0.25)
s.data_print()






