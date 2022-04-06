#Web Server : 클라이언트와 통신이 가능한 Web Server 운영하기
#CGI(Common Gateway Interface) 
#- 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약으로 대화형 웹 페이지 작성 가능
#- DB 자료 처리, form tag를 사용한 자료 전송 가능

#HTTPServer를 가지고서는 HTML 문서를 보여주기만 가능
#server에서 python을 사용해 sql문을 넘기는 등은 불가능 이런 것을 하려면 CGI가 필요한데 CGI는 CGIHTTPRequestHandler를 import해야 한다
from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8888
 
class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

#127.0.0.1은 자신 혼자만 들어갈 수가 있다
#http://127.0.0.1:8888/main.html
serv = HTTPServer(("127.0.0.1", PORT), Handler)

print("웹 서비스 시작...")

#어제 echo server를 무한루프 돌려서 시작한 거랑 같음
serv.serve_forever()






