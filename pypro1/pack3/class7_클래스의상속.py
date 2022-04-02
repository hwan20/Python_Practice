#자원의 재활용을 목적으로 클래스의 상속 - 다형성(상속나오면 무조건)

class Animal:
    def __init__(self):
        print("Animal 생성자")
    def move(self):
        print("움직이는 생물")

class Dog(Animal): #클래스를 상속받기 위해서는 괄호 안에 부모 클래스의 이름을 적는다 java의 extends 개념
    def __init__(self):
        #자바라면 super() 가 있음
        print("Dog 생성자")
    
    def my(self):
        print("난 몽몽이라고 해!")

dog1 = Dog() #Dog의 생성자를 부름 없으면 부모의 생성자를 사용
            #자식의 생성자가 있으면 부모의 생성자를 사용하지 않음 생성자의 내용이 없으면 적지 않아도 됨. 그러면 생성자 수행을 안 함. 프로그램은 돌아감
#class Dog:
#dog1. Obj를 상속받지만 Animal을 상속받지 않는 이상 사용 가능한 명령어가 아무것도 없음 
dog1.move()
dog1.my()

print()
class Horse(Animal):
    #상속받은 내용을 그대로 사용하려면 굳이 다른 내용을 적지 않아도 상관 없다
    pass

horse = Horse()
horse.move()

















