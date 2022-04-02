
class TestClass():
    
    b=1
    
    def __init__(self):
        print("이것은 생성자이다. 생성자의 내용이 없으면 생성하지 않아도 상관 없다. 또한 객체 생성시 초기화를 담당한다. 최초 1회만 호출된다")
    
    def test1(self):
        name="안녕 내 이름은 최일환이야."
        print(name)
        print(self.b)

a = TestClass ()
print(a.b)
print(a.test1())

