#단순 Client Server
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) #소켓의 종류, 소켓의 유형 기본
clientSock.connect(("127.0.0.1", 8888)) #전 세계 공통 홈 ip 127.0.0.1 포트 번호는 물리적이 X 논리적인 번호
clientSock.send("안녕 반가워".encode(encoding = "UTF_8", errors = "strict")) #UTF_8로 인코딩하고 에러를 엄하게 보겠다 - 강한 명령어인듯?
#print("from client message : ", conn.recv(1024).decode()) 위에서 send로 보낸 메세지는 server에서 conn.recv로 받을 수 있다 
clientSock.close()

#통신시 Client가 connect 하게 되면 Server에서 accept하여 통신 연결을 하게 됨
#send할 때는 2진수로 encoding된 정보들이 직렬 통신하게 됨
#recv할 때는 2진수로 encoding된 정보를 decoding하여 출력

#server를 띄어놓고 기다릴 때 client에서 연결을 주면 데이터 송수신이 됨
#server가 계속 동작되게 하고 싶으면 무한 루프에 빠뜨리고 계속 돌아가게 하면 됨
#한 명당 하나의 socket이 할당되며 데이터를 받아오고 해당 데이터를 원하는 client에게 전달하는 곳이 server이다
#client가 파일 다운로드를 요청할 때 파일을 넘기는게 ftp이다 file transfer protocol
#근데 이때 client가 요청하는 파일이 html이면 server는 web server라고 한다
#apach tomcat은 http server에서 응용 프로그램을 올릴 수 있는 2가지 기능이 다 들어있다
#그 2가지 기능이 java, jsp 언어 이며 이를 was라고 한다 web application server
#클라이언트가 서버에 요청하는 파일이 html일 때 java의 jdk가 필요없다
#그런데 클라이언트가 jsp, servlet을 요청하면 안에 java가 있으니 해석을 못 함
#그래서 필요한게 http server + 응용 프로그램이 있어야 한다. 이 용도로 사용한게 tomcat server 







