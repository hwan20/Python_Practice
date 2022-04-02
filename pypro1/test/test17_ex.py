#키보드를 통해 직원 자료를 입력 받아 가공 후 출력하는 함수 문제
#import time
#print(time.localtime()) #연도수를 빼고 싶으면 tm_year사용하면 된다
    

a=[] #list형식을 받기 위하여 선언

def inputfunc():
   
    while True : #반복문을 무한으로 돌리기 위해
        b=input("사번, 이름, 기본급, 입사년도를 순서대로 입력하세요. : ").split(",") #입력받은 값들을 , 로 구분하여 a에 담기
        a.append(b) #a에 담긴 요소들을 datas []에 list형태로 담기
        cont=input("계속 입력하시겠습니까?(y/n) : ")

        if cont == "n": #n을 입력하면 반복문 빠져나가기
            break
        elif cont == "y": #y를 누르면 속해있는 최상단으로 가는 continue 명령어로 인해 다시 시작하기
            continue
            #다른 입력값을 받았을 때 다시 if문을 반복시키는것은 return 시키면 되나?
            #혹은 break를 불러서 다시 if문으로 오도록
    return a #함수는 리턴 값이 없으면 none을 출력하므로 none을 리턴 값으로 주어 입력된 datas 값들을 함수 밖에서도 사용
datas = inputfunc()
print()

#급여 , 보너스 측정하는 방법?
"""
def outer2(tax): #tax는 지역 변수이다 함수 내에서만 사용 가능
    def inner2(su,dan):
        amount = su * dan * tax
        return amount
    return inner2
"""





print(inputfunc())
#print(datas[0])
#print(datas())
#print(len(datas)) #list로 저장됨
#print(datas[len(datas)-1])
#print(datas[1]) #나중에 빼낼때 인덱싱이 잘 되나 확인



