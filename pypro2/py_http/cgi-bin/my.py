#웹용 파이썬 모듈 : 요청시 정보를 달고 넘어옴
import cgi

#get 방식으로 url로 데이터를 전달하고 받을 수도 있다 - cgi를 import해야함
form = cgi.FieldStorage()
name = form["name"].value
age = form["age"].value

print("Content-Type:text/html;charset=utf-8\n")
print("""
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>정보 받기</h2>

이름 {0}, 나이{1}

<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
""".format(name, age))






