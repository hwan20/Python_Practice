#사용자 정의 모듈 작성 및 읽기
a = 10
print(a + 10)
print("다른 작업을 하다가 외부 모듈 읽기")

print(dir()) #현재 모듈의 멤버들을 읽어들임

list1=list(range(5))
list2=list(range(6,11))

import pack2.mymod1 #같은 패키지에 있다고 하더라도 패키지명.모듈명
pack2.mymod1.listHap(list1, list2)
#print(dir()) #현재 모듈의 멤버들에 추가가 됨


def listTot(*ar):
    print(ar)
    #현재 run하는 모듈의 __name__은 __main__이 되는데
    #다른 곳에서 import해서 run하게 되면 그 module의 이름으로 바뀌게 됨
    
    
    if __name__=="__main__": #mymod1에서 불러들였을땐 조건문 실행 X
        print("이 파일이 메인이야") #불러들이지 않고 직접 실행했을 때는 메인이 됨
        #어디서 실행했느냐에 따라서 메인이 달라짐
        #if __name__=="__main__":, print("이 파일이 메인이야") 없으면 어떤게 메인인지 알 수가 없음

#다른 곳에서 import해서 사용하면 __name__=="__main__" 이 조건 성립이 안 됨 메인이 아님 그래서 메인이라는 print가 안 나옴





listTot(list1, list2)

print()
from pack2.mymod1 import Kbs
Kbs() #import한 module의 이름이 나옴

print()
from pack2.mymod1 import mbc, price
mbc()
print("price : ", price)

#아래 두 가지는 같음 방식만 다름
"""
import pack2.mymod1 
pack2.mymod1.listHap(list1, list2)

print()
from pack2.mymod1 import Kbs
Kbs()
"""

print()

import other.mymod2
print(other.mymod2.Hap(5, 3))

from other.mymod2 import Cha
print(Cha(5, 3))

import mymod3 #외부에서 가져오는 module은 패키지명 필요 X
print(mymod3.Gop(5, 3))

from mymod3 import Nanum
print(Nanum(5, 3))

