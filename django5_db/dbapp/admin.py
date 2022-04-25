from django.contrib import admin
from dbapp.models import Article

# Register your models here.
#등록된 모델을 여기다 입력시켜줘야 한다
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'price', 'pub_date')

admin.site.register(Article, ArticleAdmin) #models의 class인 Article를 import해줘야함

