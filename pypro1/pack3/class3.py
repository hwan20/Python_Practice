#class
#self가 붙으면 제일 먼저 지역 변수를 찾는다. 없으면 클래스 내에서 찾고 클래스 내에도 없으면 전역으로 찾는다.
#만약 self가 붙지 않았다면 클래스 밖에서 찾는다. self가 붙어있으면 무조건 클래스 내에서만

kor = 100 #이름이 바뀌면 show 메소드의 print(kor)이 못 찾음 클래스 밖에서만 찾는다는 뜻.

def abc():
    print("함수라고 해")
    
class MyClass:
    kor = 90 #이름이 바뀌면 show 메소드의 print(self.kor)이 못 찾음. self가 붙으면 클래스 내에서만 찾는다는 뜻
    
    def abc(self):
        print("난 메소드야")

    def show(self):
        #kor = 88 
        print(self.kor) #self가 붙어 해당 객체 안에 있는 kor을 찾음
        print(kor) #메소드 내에 있는 지역 변수를 찾음 88이 나옴 
                    #show 안에 kor이 없으면 class밖에서 kor찾음 100이 나옴
        self.abc() #class에 있는 abc를 찾음
        abc() #module에 있는 abc를 찾음
                #class의 멤버는 self로 찍음. java의 this 개념
                
        
my = MyClass()
my.show()
print(my.__dict__) #아무것도 없는 이유는 MyClass 타입의 my 인스턴스에 아무것도 넣지 않고 부르기만 해서.


print("-----------------")
class OurClass:
    a=1
    
print(OurClass.a)

our1=OurClass()
print(our1.a)

our2=OurClass()
print(our2.a)
our2.b=2 #클래스 내에 없는 변수명이라도 생성된 인스턴스에 변수명을 생성하고 값도 같이 넣을 수가 있다
print(our2.b)
print(our2.__dict__) #확인해 보면 a는 our2.a로 호출하기만 했으니 값이 없지만 b는 our2.b=2로 값을 입력해서 b=2라는 변수가 있다 

#print(our1.b) #에러









