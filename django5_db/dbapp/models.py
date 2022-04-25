from django.db import models

# Create your models here.
#table 선언 - 반드시 여기서 선언
class Article(models.Model):
    code = models.CharField(max_length = 10) #varchar 생각하면 됨
    name = models.CharField(max_length = 20) #내부적으로 sql문으로 해석됨 create name varchar(20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    #만든 데이터 타입은 4개이지만 PK 타입의 ID가 하나 자동으로 생성되어 총 5개가 생성된다 






