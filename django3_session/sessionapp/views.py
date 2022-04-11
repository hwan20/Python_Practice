from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def mainFunc(request):
    return render(request, "main.html" )

def setOsFunc(request):
    #print('request GET : ', request.GET) #<QueryDict: {}> 아직 만들지는 않았으나 dict 타입으로 출력됨
    
    if "favorite_os" in request.GET: #request.GET 안에 있는 Dict에 favorite_os가 있으면 True
        print('request GET : ', request.GET["favorite_os"]) #selectos에서 클릭한 데이터가 get방식으로 넘어옴
        
        #request.session["세션키"]로 session을 만들 수가 있다
        #접속되는 곳에 f_os라는 이름의 session이 생성되고 클라이언트가 선택한 os의 정보를 집어넣음 4시 45분 8분
        request.session['f_os'] = request.GET["favorite_os"] #선택한 정보가 넘어오는 것은 request.GET["변수명"]에 담겨있다
        return HttpResponseRedirect("/showos") #redirect 방식 (client를 통해서 요청을 하는 것)
    
    #선택한 get방식에 favorite_os 정보가 있으면
    else:
        return render(request, "selectos.html") #forward 방식 (server가 직접 파일을 선택해서 client로 전송(push)하는 것)

#client가 요청하면 메인을 만나고 요청명에 해당하는 비즈니스 로직을 수행
#server가 push하는 것은 해당 요청을 직접 push함    
    
def showOsFunc(request): #return HttpResponseRedirect("/shows") 요청이 main urls로 넘어가니 만날 수 있던 요청
                        #forward 요청이었으면 못 만남
    
    dict_context = {}

    if "f_os" in request.session:
        print("유효 시간 : ", request.session.get_expiry_age())
        dict_context['select_os'] = request.session['f_os'] #dict 타입으로 select_os라는 key와 f_os라는 value값이 들어감
        dict_context['message'] = "그대가 선택한 운영 체제는 %s" %request.session['f_os']
    else:
        dict_context['select_os'] = None
        dict_context['message'] = "운영 체제를 선택하지 않았다"
    
    #del request.session['f_os'] #세션 삭제
    request.session.set_expiry(5) #세션 유효 시간을 5초로 제한
    
    return render(request, "show.html", dict_context)



