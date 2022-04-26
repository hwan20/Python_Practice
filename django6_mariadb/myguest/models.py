from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno = models.AutoField(auto_created = True, primary_key = True) #자동으로 생성되는 아이디 말고 내가 지정해 주고 싶으면
    title = models.CharField(max_length = 50)
    content = models.TextField() #CharField보다 많은 내용을 작성하기 위해 TextField 사용
    regdate = models.DateTimeField()
    

    class Meta:
        #ordering=('title',)
        #ordering=('-title',)
        ordering=('id',) #models안에서 정렬하는 방법을 추천
        