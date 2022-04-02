#완성 제품의 부품 클래스로 사용될 클래스로 핸들이라고 가정하자

class PohamHandle:
    quantity = 0 #회전량
    
    def LeftTurn(self, quantity): #quantity가 음수이면 좌회전으로 가기로 함
        self.quantity = quantity
        return "좌회전"
        
    def RightTurn(self, quantity): #quantity가 양수이면 좌회전으로 가기로 함
        self.quantity = quantity
        return "우회전"




