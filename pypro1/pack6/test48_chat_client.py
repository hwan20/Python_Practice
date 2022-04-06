#멀티 채팅 클라이언트 : socket, thread

import socket
import threading
import sys

#서버와 채팅을 주고 받는 것을 threading으로 관리하기

def handle(socket): #파이썬의 표준 출력은 버퍼링이 된다 (계속 쌓인다)
    
    while True: #무한 루프로 데이터를 계속 받음
        data = socket.recv(1024) #기본은 1kb 단위
        #print(data.decode("UTF_8")) #전송하는 데이터가 없더라도 계속 받으니 if문을 걸어줌 
        
        if not data:continue #데이터가 있을 때만 진행함
        print(data.deccode("UTF_8"))

sys.stdout.flush() #쌓이는 표준 출력인 buffer를 지워줌

name = input("채팅명 입력 : ")
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(("192.168.219.103", 5555))
cs.send(name.encode("UTF_8")) #채팅명을 먼저 넘겨줌 send를 사용해서 넘겨줌

th = threading.Thread(target=handle, args=(cs,))
th.start()

while True:
    msg = input() #채팅 메세지(수다) 입력
    sys.stdout.flush()
    if not msg:continue #메세지를 입력하지 않으면 send하지 않음
    cs.send(msg.encode("UTF_8"))

cs.close()









