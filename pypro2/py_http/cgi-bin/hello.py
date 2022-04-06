#웹용 파이썬 모듈

a = 10
b = 20
c = a + b
mbc = "파이썬 만세"

#아래의 내용만 사용하는 게 끝이 아님 위의 python 변수 내용도 사용

print("Content-Type:text/html;charset=utf-8\n")
print("<html><body>")
print("<b>안녕하세요</b> 파이썬 모듈로 작성한 문서입니다<br>")
print("<hr>")
print("합은 %d"%(c,)) #print(c) 로 주면 콘솔창에 나옴 이렇게 블록 안에 넣어줘야 함
print("<br>메세지는 %s"%mbc)
print("<p>작성자 : 홍길동")
print("</body></html>")






