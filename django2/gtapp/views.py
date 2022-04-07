from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect

# Create your views here.

def mainFunc(request):
    return render(request, "index.html")

class CallView(TemplateView):
    template_name = "callget.html"
"""
insert창이 나오는 곳
def insertFunc(request):
    return render(request, "insert.html")

insert작업이 이루어지는 곳
def insertokFunc(request):
    #name = request.GET.get('name') #request로 넘어오는 데이터를 받아옴
    name = request.GET['name'] #위와 같음
    print(name)
    return render(request, "list.html", {'name':name}) #어떤 일을 하다가 html안에 넣어줘야 할 때 dict 타입으로 작성하여 전달한다
"""
    
"""
    member 요청에 의해 main urls에서 gtapp urls로 위임을 시키고
    gtapp urls에서 member/insertok 요청에 대해서 insertFunc 동작을 하게 함
    insertFunc는 받은 요청에 대해서 list.html이 보여주도록 이동시킴 
"""

#insert창과 insert작업이 이루어지는 곳을 같이 묶기 위해
def insertFunc(request):
    if request.method == 'GET': #insert페이지에 가면 이 부분이 수행됨
        print("GET요청 처리")
        return render(request, "insert.html") #forward 방식
    
    elif request.method == 'POST': #form 태그에서 데이터를 전송하면 이 부분이 수행됨
        print("POST요청 처리")
        name = request.POST['name']
        #return render(request, "insert.html")
        return render(request, "list.html", {'name':name})
    else:
        print('요청 에러')
"""
    그전에는 요청 명으로 insert 페이지와 insertform 페이지를 나눴었는데
    지금은 데이터 넘어오는 방식으로 insert페이지와 insertform 페이지를 나눔
    넘어오는 데이터의 방식이 GET 방식이면 insert 페이지
    넘오오는 데이터의 방식이 POST 방식이면 insertform페이지
"""
