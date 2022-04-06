#단순 Client Server

import socket

#소켓 객체 생성
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓의 종류, 소켓의 유형 기본
clientSock.connect(("127.0.0.1", 7878)) #내 IP주소를 줘도 됨 192.168.219.103
clientSock.sendall("안녕 서버~".encode("UTF_8"))
re_msg = clientSock.recv(1024).decode() #buffer size 전달온 메세지를 받음
print("수신 자료 : ", re_msg)
clientSock.close()






