class CoinIn:
    coin = int(input('동전을 입력하세요 :'))
    change = 0
    cupCount = int(input('몇 잔을 원하세요 : '))


    def culc(self):
        self.change = self.coin - 200*self.cupCount
        return [self.change,self.coin,self.cupCount]

class Machine:

    cupCount = 1

    result1 = CoinIn()
    result = result1.culc()

    def showData(self):

        change = self.result[0]
        self.cupCount = self.result[2]
        if change < 0:
            print('요금 부족')
        else:
            print('커피 {}잔과 잔돈 {} 원'.format(self.cupCount,change))

a = Machine()

a.showData()