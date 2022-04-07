#main urls.py로부터 위임받은 urls이다

from django.urls import path
from gtapp import views #같은 영역이라도 import 해야함

urlpatterns = [
    path('insert', views.insertFunc),
    #path('insertok', views.insertokFunc),
]
