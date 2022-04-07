"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #누간가가 ip와 port번호만 주고 아무것도 안 줄때 서버를 구동하면 import한 views의 indexFunc함수를 구동함
    path('', views.indexFunc), #요청명이 없을 때.   myapp에 있는 views를 import한다 index는 함수명
    
    #요청명은 아무렇게나 줘도 상관 없다
    #요청명, 함수 순
    path('good', views.showFunc), #요청명 - http://127.0.0.1:8000/good -> 이 요청명
    
    
    #주소창에 path에 해당하는 요청명이 들어오면 작성한 함수가 작동하게 된다
    #위는 good이라는 요청명에 대해 views.py 클래스의 showFunc함수가 작동한것
    #showFunc는 들어오는 작업을 show.html로 작업을 forward 이동시키고
    #client 화면에는 show.html이 보이게 된다
    #주소창에는 show.html이 아닌 호출명인 good이 나오게 되는 것.
    #(client가 요청하는게 아니고 server가 보낸것 - 이것이 렌더링) 
    
    
    
]












