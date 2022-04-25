from django.shortcuts import render
from dbapp.models import Article

# Create your views here.

def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    #Django ORM 사용 select * from article
    #sql의 select 문을 사용할 수가 있지만 불편하니 호환해주는 ORM을 사용한다
    datas = Article.objects.all() 
    print(datas, type(datas)) #<class 'django.db.models.query.QuerySet'>
    print(datas[0].name)
    return render(request, 'list.html', {'articles':datas})

