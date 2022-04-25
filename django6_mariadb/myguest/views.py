from django.shortcuts import render
from myguest.models import Guest

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


