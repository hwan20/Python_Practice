from django.shortcuts import render, redirect
from myguest.models import Guest
from _datetime import datetime
from django.http.response import HttpResponseRedirect
#from django.utils import timezone #둘 중 아무거나 사용

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    print(Guest.objects.filter(title__contains = 'ㅎㅇ')) #
    print(Guest.objects.filter(id=1)) #pk는 중복되는 데이터가 없다
    print(Guest.objects.filter(title='난 prompt야')) #중복되는 데이터가 있을 수 있다
    print(Guest.objects.get(id=1))
    
    gdatas = Guest.objects.all()
    #gdatas = Guest.objects.all().order_by('title') #ascending sort
    #gdatas = Guest.objects.all().order_by('-title') #decending sort
    #gdatas = Guest.objects.all().order_by('-id', 'title') #id:descending,  title:ascending 아이디가 같으면 타이틀별로
    #gdatas = Guest.objects.all().order_by('id', 'title')[0:2] #인덱싱하여 보여줌
    
    return render(request, 'list.html', {'gdatas':gdatas})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == "POST":
        #print(request.POST.get("title"))
        #print(request.POST["title"]) #위와 같음
        Guest(
            title = request.POST.get("title"), #title은 테이블의 칼럼명이고 "title은" insert.html에 있는 변수명이다
            content = request.POST.get("content"),
            regdate = datetime.now()
            #regdate = timezone.now()
        ).save() #SQL문의 INSERT INTO와 같다 
        
    #return HttpResponseRedirect('/guest')
    return redirect('/guest') #위와 같음
    #추가, 수정, 삭제는 서버가 요청을 하는 것이 아니고 client를 통해서 요청을 하는 것이다
    
#수정
"""
gtab = Guest.objects.get(id=해당 아이디)
gtab.title = '수정 제목'
gtab.content = '수정 내용'
gtqb.save()   "UPDATE TABLE명 set ~~"
"""

#삭제
"""
gtab = Guest.objects.get(id=해당 아이디)
gtab.delete()   "DELETE FROM 테이블명 ~~"
"""
        
        
