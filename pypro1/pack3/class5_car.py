# 완성된 부품들을 조립하여 완성된 차를 만듦
# 여러 개의 부품 클래스를 이용해 완성된 클래스를 만든다

import pack3.class5_handle

class PohamCar: #()는 상속이 있을 때 쓰고 없을 땐 안 써도 된다
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        self.ownerName = ownerName #self.ownerName은 전역 변수에 있는 ownerName을 지칭하는데 전역 변수에 없는 변수이면 외부에서 들어오는 값을 지칭한다
        self.handle = pack3.class5_handle.PohamHandle() #이것을 class의 포함관계 라고 한다

    def TurnHandle(self, q):
        if q > 0: #회전량이 양수이면 오른 쪽으로 가기로 함
            self.turnShowMessage = self.handle.RightTurn(q) #.이 두 개 이상으로 늘어나면 포함 관계라고 생각하면 된다
                                    #같은 클래스 내에 있는 메소드의 변수 명도 가져올 수가 있다?
        elif q < 0:
            self.turnShowMessage = self.handle.LeftTurn(q)
        elif q == 0: #else만 써도 상관 없지만 q가 0값 이라는 것을 보여주기 위해
            self.turnShowMessage = "직진"
            self.handle.quantity = 0
            
if __name__ =="__main__": #여기가 메인 문이라는 것을 보여주기 위해
    #print(PohamCar.__dict__) Main 문이라고 적혀있음
    
    tom = PohamCar("Mr.Tom") #여기서 인자로 준 문자열이 self.ownerName의 값으로 들어감
    tom.TurnHandle(10)
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + str(tom.handle.quantity))
    
    tom.TurnHandle(0)
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + str(tom.handle.quantity))
    
    print()
    sujan = PohamCar("Ms.Sujan")
    sujan.TurnHandle(-15)
    print(sujan.ownerName + "의 회전량은 " + sujan.turnShowMessage + str(sujan.handle.quantity))
    
    
    print(PohamCar.__dict__)
    
    