#멀티 채팅 서버 : socket, thread를 이용해서 다른 사람과 채팅하기

"""
python은 내부적으로 multi process를 사용할 수가 없다
gil이라는 내부 모드 때문인데
그래서 python에서는 thread 대신에 pool이라는 병렬 처리로 작업한다
"""


import socket #server용과 client용 socket은 하나만 있으면 된다
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("192.168.219.103", 5555)) #내 ip번호와 port번호를 입력시켜줌. port번호는 정해진 숫자 외에 마음대로 선언 가능
ss.listen(5)
print("채팅 서버 시작")

users = [] #채팅 접속한 컴퓨터의 소켓 갯수만큼 담기

def chatUser(conn):
    name = conn.recv(1024)
    data = "^<^" + name.decode("UTF_8") + "님이 입장하셨습니다" #제일 먼저 채팅명이 넘어옴
    print(data) #server에 채팅명을 print로 찍음. 하지만 server에 찍는게 중요한게 아니고 client한테 보여줘야함
    
    try:
        for p in users:
            p.send(data.encode("UTF_8")) #모든 접속자에게 접속 채팅명을 전송
        
        while True: #채팅을 주고 받는 메세지 전송 방. 모든 접속자에게 메세지를 전송 
            msg = conn.recv(1024) #1024는 버퍼 사이즈 #thread에 의해 전송함. A컴퓨터의 conn.recv이 될 수도, B컴퓨터가 될 수도 있다 
            data = name.decode("UTF_8") + " 님 메세지 : " + msg.decode("UTF_8")
            print(data)
            for p in users:
                p.send(data.encode("UTF_8"))
    except:
        users.remove(conn) #채팅을 종료한 클라이언트 소켓을 제거
        data = "~~ "+name.decode("UTF_8") + "님 퇴장하셨습니다."
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode("UTF_8"))
        else:
            print("exit")
    
while True:
    conn, addr = ss.accept() #클리이언트가 컨넥트 하는 순간 ss.accept를 만남 그 정보를 conn과 addr에 담음
    users.append(conn) #실제 넘어오는 메세지는 conn이다. conn으로 센드 리시브 모두 가능
    #client의 socket이 conn이 되는 것
    
    #계속해서 데이터를 주고 받기 위해 thread 클래스를 사용
    th = threading.Thread(target = chatUser, args=(conn,)) #클라이언트의 소켓과 서버의 소켓이 통신을 주고 받음
    #A컴퓨터가 접속하면 A컴퓨터의 socket이 chatUser의 conn으로 들어감
    #접속하는 client컴퓨터의 갯수만큼 thread가 생성되며 chatUser를 각각 호출함
    
    
    
    
    
    






