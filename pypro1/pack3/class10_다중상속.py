#다중 상속 하나의 클래스에 두 개 이상의 부모
#순서가 중요하다

class Donkey:
    data = "당나귀 만세"
    
    def skill(self):
        print("당나귀 : 짐 나르기")

class Horse:
    def skill(self):
        print("말 : 달리기")

    def hobby(self):
        print("프로그램 짜기")

class Mule1(Donkey, Horse): #하나 이상의 클래스를 상속받을 때는 순서가 중요
    pass

mu1 = Mule1()
print(mu1.data)
mu1.skill() #같은 메소드 명을 가질때 먼저 상속받은 클래스에게 우선 순위가 있다
mu1.hobby()

print("---------------------")
class Mule2(Horse, Donkey):
    def play(self):
        print("노새 고유 메소드")

    def hobby(self):
        print("노새는 걷기를 좋아해")

    def showHobby(self):
        self.hobby() #Mule2의 hobby가 나오겠지?
        super().hobby() #Horse의 hobby가 나오겠지?
        print(self.data, super().data)

mu2 = Mule2()
mu2.skill()
mu2.hobby()
mu2.play()
mu2.showHobby()















