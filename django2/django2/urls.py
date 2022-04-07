"""django2 URL Configuration

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
from gtapp import views
from gtapp.views import CallView
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Function views 요청이 없을 때 함수를 부름
    path('',views.mainFunc), #요청이 없을 때 gtapp의 mainFunc파일을 호출하고 mainFunc는 forward이동시켜 출력한다 
    
    #Class-based views 요청명이 있을 때 클래스를 부름  **굳이 안 들어감
    path('abc/callget', CallView.as_view()), #CallView는 TemplateView를 상속 받아서 as_view가 있다
    
    #Including another URLconf 위임
    path('member/', include('gtapp.urls')), #메인 urls에서 각 app에 있는 urls로 역할을 분담시킴 member요청명에 대해 이쪽으로 넘김
    
    #아무런 요청이 없을 때는 gtapp의 views에 있는 mainFunc를 forward이동해서 보여줌 - Funcction views 방법
    #요청명이 abc/callget일 때는 CallView의 템플릿을 보여줌 - Class-based views 방법
    #어떤 app의 메인 요청명이 있을 때 그걸 해당 app의 urls에 위임시킴 메인 urls에는 Function views 방식이 적을 수록 좋다
]









