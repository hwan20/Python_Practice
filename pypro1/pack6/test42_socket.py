#파이썬 네트워크(정확히는 통신을 주고 받는 네트워킹)
#네트워크를 위한 통신 채널을 지원 : socket 모듈

import socket

#socket.했을 때 나오는 것은 function 혹은 class 혹은 전역 변수이다 why? import하는 것은 module이고 module안에 있는 3가지를 쓸수 있으니
#getservbyname(servicename[, protocolname]) -> integer 서비스 네임과 protocol 이름을 적으면 포트 번호를 리턴한다
#0부터 1024까지는 시스템에서 스는 포트 번호로 사용 X

#통신에 사용되는 모델에는 여러 종류가 있다
print(socket.getservbyname("http","tcp")) #80 -> 아무나 들어갔다 나갈 수 있음. 회사에서는 80을 안 씀
print(socket.getservbyname("telnet","tcp")) #23 잘 안 씀
print(socket.getservbyname("ftp","tcp")) #21
print(socket.getservbyname("smtp","tcp")) #25
print(socket.getservbyname("pop3","tcp")) #110

#socket.getaddrinfo(host, port, family X, type X, proto, flags X)
print(socket.getaddrinfo("www.naver.com", 80, proto = socket.SOL_TCP)) 
#223.130.200.107, 223.130.195.200 번호를 이용해서 해당 컴퓨터를 쫓아가는 것은 쉽다
#https://223.130.200.107.index.html 을 입력하면 네이버 홈페이지에 들어갈 수 있다










