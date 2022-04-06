#단순 Echo Server

from socket import *

#socket을 import해서 사용 가능
serverSock = socket(AF_INET, SOCK_STREAM) #socket(소켓의 종류, 소켓 유형)
serverSock.bind(("127.0.0.1", 8888)) #소켓 객체를 소켓에 바인드 시킴
serverSock.listen(1) #연결 정보수를 전달함. 연습용이라 일회용으로 할 거니 1일 사용
print("Server Start...")

conn, addr = serverSock.accept() #임의의 다른 컴퓨터에서 접속 요청이 올 때까지 대기
print("client addr : ", addr)

#클라이언트로부터 2진법으로 인코딩되어 받은 메세지를 해석을 해서 출력
#conn.recv 하면 들어오는 메세지를 받아온다. 1024는 1kb로 기본 값이다
print("from client message : ", conn.recv(1024).decode()) 
conn.close()
serverSock.close()



