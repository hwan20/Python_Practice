from django.db import models

# Create your models here.

class Maker(models.Model):
    mname = models.CharField(max_length = 10) #회사명의 최대 길이는 10자리
    tel = models.CharField(max_length = 30)
    addr = models.CharField(max_length = 50)
    
    class Meta:
        ordering = ('-id',) #id디센딩? tuple타입이라 ,찍음
    
    #어드민 화면에서는 아래와 같이 있어야 편함 - ?
    def __str__(self):
        return self.mname

class Product(models.Model):
    pname = models.CharField(max_length = 10) #회사명의 최대 길이는 10자리
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete=models.CASCADE) #-> 물리적으로는 maker_name
    #Maker테이블의 아이디를 참조하는 테이블
    #on_delete=models.CASCADE
    #A테이블의 어떤 정보를 B테이블에서 참조하여 작성할 시 Primary Key를 가지고 Foreign Key를 작성함
    #이때 B테이블에서 참조한 A테이블의 정보를 삭제할 시 B테이블에서 참조한 정보까지 삭제하게 하는 기능 