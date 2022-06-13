from django.db import models

# Create your models here.

class BoardTab(models.Model):
    name = models.CharField(max_length = 20) #작성자
    passwd = models.CharField(max_length = 20) #비밀번호
    mail = models.CharField(max_length = 30) #이메일
    title = models.CharField(max_length = 100) #글 제목
    cont = models.TextField() #글 내용
    bip = models.GenericIPAddressField() #글을 올린 사람의 ip번호
    bdate = models.DateTimeField() #작성일
    readcnt = models.IntegerField() #조회수
    gnum = models.IntegerField() #답글과 원글을 그룹으로 묶기 위해 사용  a게시물 1개 gunm1, b게시물 4개 gnum2, 3게시물 1개 gnum6
    onum = models.IntegerField() #원글의 답글과 답글의 답글 순서를 정하기 위해 사용
    nested = models.IntegerField() #들여쓰기 하기 위해 사용 ex) 원글은 0, 원글의 답글은 1, 원글의 답글의 답글은 2 이런 식
    #ID까지 넣어서 12개의 columns MariaDB에서 desc myboard_boardtab;를 확인하며 Auto로 상승하는 칼럼이 보임
    #답글이 달리면 원글과 같은 그룹으로 묶임
    