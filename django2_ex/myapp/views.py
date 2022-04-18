from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "main.html")

def transFunc(request):
    if request.method == 'GET': #if를 사용해야 함 request.method 는 bool type으로 T와 F를 반환 GET이면 T POST면 F
        gender = request.GET['gender']
        return render(request, "show.html", {'gender':gender})
    else:
        print('요청 에러')

