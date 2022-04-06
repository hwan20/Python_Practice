#Echo Server : 서비스를 계속 유지 시킨다

import socket
import sys

#HOST = "127.0.0.1"
HOST = "" #공백으로 줘도 사용 가능한 주소가 찾아감 
PORT = 7878

#serverSock = socket(AF_INET, SOCK_STREAM) #소켓의 종류, 소켓의 유형 기본
#아까는 import socket * 해서 모두 사용했지만 지금은 다름
serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    #현재는 싱글 스레드, 여러 사람과 통신을 주고 받기 위해서는 멀티 스레드를 사용해야 함
    serSock.bind((HOST,PORT)) #server socket에 tuple 타입으로 바인딩해줘야 함
    serSock.listen(5) #동시 최대 접속 수 : 1~5 -> 5명이 동시에 접속 가능한게 X 동시에. 10~20명도 동시 접속 가능
    print("서버 서비스 중....")
    
    while True: #와일문을 돌려 서버를 계속 유지 시키기 위해 무한루프를 돌림
        conn, addr = serSock.accept() #accept는 클라이언트가 connect하는 순간 승인하는 것
        print("client info : ", addr[0], addr[1]) #클라이언트가 누군지 알기 위해 addr을 씀 addr에 접속 정보가 있다
        #addr[0] 클라이언트의 주소 addr[1]은 포트번호 
        print(conn.recv(1024).decode()) #메세지 수진
        
        #메세지 송신
        conn.send(("from server : " + str(addr[1]) + ", 너도 잘 지내").encode("UTF_8"))
        
        
except Exception as e:
    print("err : ", e)
    sys.exit()#에러가 나면 동작을 정지시킴
finally:
    serSock.close()
    conn.close()

