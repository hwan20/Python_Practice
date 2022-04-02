#클래스는 새로운 타입을 만든다
#클래스는 속성과 행위로 구성되어 있다 속성 - 변수 행위 - 메소드 
#변수 : 속성, 상태, 필드 등이라고 말 한다

class Singer:
    title_song = "화이팅 코리아"
    
    def sing(self):
        msg = "노래는 "
        print(msg, self.title_song, "랄랄라~")
        
    def hello(self):
        msg = "안녕하세요 "
        print(msg+"저 가수예요")

    #등등 밑에 있음

#------아래 내용은 별도의 모듈을 만들었다 가정------

bts = Singer() #Singer 클래스의 인스턴스 주소 값을 가져옴
bts.sing()
bts.hello()

print("---------------------------------")
blackpink = Singer()
blackpink.hello()
blackpink.sing()
blackpink.title_song = "마지막 처럼"
blackpink.sing()
blackpink.co = "SM" #이렇게만 해도 blackpink 객체에 co라는 함수가 생김
print("blackpink 소속사 : ", blackpink.co)

#print("bts 소속사 : ", bts.co) #bts.co에 아무 값도 안 줘서 없음
bts.sing()

print(id(bts), id(blackpink))
print(type(bts), type(blackpink))
print(bts.__dict__, blackpink.__dict__)
print(dir(bts), dir(blackpink))



