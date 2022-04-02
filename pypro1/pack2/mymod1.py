#사용자 정의 모듈 : 독립적으로 사용하지 않고 다른 모듈에서 호출될 대상

price = 12345

def listHap(*ar):
    print(ar)
    if __name__=="__main__": #실행한 곳의 module이름이 "__main__"에 들어감 
        print("이 파일이 메인이야") #메인 모듈이 아니라서 실행 X
        
def Kbs():
    print(__name__) #현재 module의 이름이 출력이 됨

def mbc():
    print("문화방송 : 11")


print(listHap())
print(Kbs())



