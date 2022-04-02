#Singer 타입의 객체
#abc라는 가수 객체

import pack3.class4

def process():
    abc=pack3.class4.Singer()
    print("타이틀 송 : ", abc.title_song)
    abc.sing()
    abc.hello()
    print(__name__)

if __name__=="__main__": #이 클래스가 메인 문이라는 뜻이다.
    process()

