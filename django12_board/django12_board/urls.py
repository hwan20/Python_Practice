"""django12_board URL Configuration

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
from myboard import views
from myboard.views import view1 #이런 식으로도 경로를 설정할 수가 있다
#MVC패턴이 django에서는 MTV패턴이다 컨트롤러 역할인 views는 여러 개를 만들 수가 있다 - views를 대신할 패키지를 만들면 메인 views는 사용 못 하는 듯?? 
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', view1.mainFunc),
    path('board/', include('myboard.urls')), 
    #include방식으로 경로를 정해줌 board로 들어오는 경로는 myboard 앱의 url로 경로 지정
    
]
