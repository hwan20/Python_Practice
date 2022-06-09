from django.db import models

# Create your models here.

class BoardTab(models.Model):
    name = models.CharField(max_length = 20)
    passwd = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    cont = models.TextField()
    bip = models.GenericIPAddressField() #글을 올린 사람의 ip번호
    bdate = models.DateTimeField()
    readcnt = models.IntegerField() #들여쓰기
    gnum = models.IntegerField() #
    onum = models.IntegerField() #
    nested = models.IntegerField() #
    #ID까지 넣어서 12개의 columns MariaDB에서 desc myboard_boardtab;를 확인하며 Auto로 상승하는 칼럼이 보임
    
    