#상속
#클래스는 별도의 모듈로 만들어야 하는데 테스트 용이라 그냥 진행

#상속 받은 클래스를 상속 받는 클래스로 만듬
class Person: #최상위 클래스
    say = "나는 사람이야~"
    nai = 20
    __abc = "good" #private 변수 명에 __를 주면 다른 곳에서 사용하지 못 한다
    
    #a = print("이게 되나?") 이건 불려지지 않음. run하는 시점에서 클래스를 한 번 읽고 출력하는 듯
    
    def __init__(self,nai): #생성자는 초기화를 담당하고, 10시 33분 설명~~~~~~
        print("person 생성자")
        self.nai = nai
        #self.nai는 전역 변수인 nai와 다르다
        
    def printInfo(self): #self와 java의 this를 비교
        print("나이 : {}, 이야기 : {}".format(self.nai, self.say)) #입력받은 nai와 say를 여기에 출력

    def hello(self):
        print("안녕")
        print(self.__abc)
    
    @staticmethod #이렇게 사용하면 staticmethod가 된다. 스프링에서는 어노테이션, python에서는 데코레이터
    def sbs(tel):
        print("sbs _ static method", tel)
        
        
#Person.hello 는 불가능하다 self를 만족시키지 못 하기 때문
print(Person.say, Person.nai)
p = Person(22) #이때 Person의 클래스를 본따스 p클래스가 새로 생성되면서 생성자의 변수(nai)에 22가 들어간다
p.printInfo() #p의 객체 변수가 printInfo()에 들어감 새로 생성된 객체에 printInfo self가 들어가기 때문에 p에는 nai=22가 생긴다
print(p.__dict__)
p.hello()

print("***" *10)
class Employee(Person): #이 클래스의 부모 클래스는 Person
    say = "일하는 동물" #부모의 멤버는 자식의 멤버에 의해 가려짐. 명시적으로 호출하지 않는 이상 자식의 멤버가 불림. 이를 은닉화라고 한다
    subject = "근로자"
    
    def __init__(self):
        print("Employee의 생성자로 초기화를 담당하고 변수 어쩌고저쩌고")
    
    def printInfo(self): #method overriding 메소드의 재정의. 부모 클래스에 있는 메소드에 덮어쓰기함
        print("Employee 클래스 내의 printInfo")
        
    def eprintInfo(self):
        #printInfo()는 모듈의 fun을 부름. self.이 있으면 현재 클래스의 메소드를 찾고 없으면 부모에게 감 
        self.printInfo() #eprintInfo를 실행하면 자기의 printInfo를 호출하는 거라서 ("Employee 클래스 내의 printInfo") 출력함 만약 없으면 부모 클래스에서 찾아옴
        super().printInfo() #부모 클래스에 있는 printInfo를 뜻함
        print(self.say, super().say) #self.say는 Employee의 say를, super().say는 Person의 say를 뜻한다
        self.hello() # Employee에 hello 메소드가 없으니 부모 클래스에서 가져옴

e = Employee()
print(e.say, e.nai) #Employee 클래스에서 say와 nai를 찾음 없으니 부모 class에서 값을 리턴해서 가져옴
e.printInfo() #Employee 클래스에서 메소드를 찾고 없으니 부모 클래스의 메소드를 가져옴
print(e.subject)
e.printInfo()
e.eprintInfo()

print("***" *10)

class Worker(Person):
    def __init__(self, nai):
        print("Worker 생성자")
        super().__init__(nai) #부모 클래스의 생성자를 명시적으로 호출함 이것을 Bound Method Call이라고 한다
        #super().이 없으면 20살로 됨 부모 클래스의 생성자를 가져옴
        
    def wprintInfo(self):
        super().printInfo()

w = Worker("25") #Worker 생성자의 변수에 25를 넣음
                #부모 클래스의 생성자 메소드에서 nai 메소드를 입력받기를 원하니 25를 안 넣으면 에러가 생김
print(w.say, w.nai) #Worker 클래스에 say가 없으니 부모 클래스에서 찾아옴, nai 클래스는 있으니 25가 생김
w.printInfo() # Worker 클래스에서 printInfo를 먼저 찾고 없으면 부모 클래스에서 찾음
w.wprintInfo() #w의 주소를 들고 wprintInfo의 self로 들어감 super().을 만나서 바로 부모 클래스의 printInfo로 찾아감

print("***" *10)

class Programmer(Worker):
    def __init__(self, nai):
        print("Programmer 생성자")
        Worker.__init__(self, nai) #unBound method call
        #Worker 생성자를 가져오는데 Worker 생성자에 Person 생성자도 있으니 두 개가 같이 찍힘

    def wprintInfo(self): #overriding 한 것임
        print("Programmer 내에 작성된 wprintInfo이다")

    def hello2(self):
        print(super().__abc)

pr = Programmer(33) #생성자의 nai 변수에 33을 전달, Programmer에는 nai 변수가 없으니 부모 클래스에 올라간다. 부모 클래스의 self.nai = nai 에서 self.nai에 33이 입력되고
                    #Programmer 객체에 nai=33이 입력된다
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()
print(pr.__dict__)

print("***" *10)
p.hello()
#pr.hello2() __abc는 private라서 상속 받고 나오더라도 programmer에서 사용할 수는 없다

w.sbs("111-1111")
pr.sbs("222-2222")
e.sbs("333-3333")

print("--------클래스 타입--------")
a = 10
print(type(a)) #a는 int 타입
print(type(pr)) #pr은 Programmer 타입
print(Programmer.__bases__) #다중 상속이 가능하기 때문에 튜플 형식으로 나옴. Programmer의 부모는 Worker
print(Worker.__bases__) #Worker의 부모는 Person
print(Person.__bases__) #최상위 클래스인 Person의 부모는 obj이다









