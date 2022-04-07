from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def indexFunc(request): #요청에 반응하는 함수는 반드시 request를 사용한다
    
    #HttpResponse 클래스로 인해 바로 내보낸것
    #return HttpResponse('요청 처리 결과') #다른 HttpResponse와 조심
    
    msg = '장고 만세~~~'
    ss = "<html><body>장고 프로젝트 구현 %s</body></html>" %msg #변수 명으로도 줄 수가 있다
    #html을 매번 부르기 귀찮기도 하고 특별한 점도 없으니 이것을 폴더에 넣어서 부름 templates -> new folder로 작성 이름은 정해진 것 바꾸면 X
    
    return HttpResponse(ss)

def showFunc(request):
    #어떤 일을 하다가 html안에 넣어줘야 할 때 dict 타입으로 작성하여 전달한다
    msg = '{{}}어떤 작업을 하다가~~'
    
                    #show.html을 부르는 것    key:value값 
    return render(request, 'show.html' ,{'mymsg' : msg}) #위와 같은 방식X 이렇게 html을 렌더링해야함 forward 방식 요청을 전달하는 것


