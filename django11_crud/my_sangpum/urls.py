from django.contrib import admin
from django.urls import path
from my_sangpum import views

urlpatterns = [
    path('list/', views.ListFunc), 
    path('insert/', views.InsertFunc), #인서트는 get이든 post든 가능 아니면 따로따로도 가능
    path('insertok', views.InsertOkFunc),
    path('update/', views.UpdateFunc), 
    path('updateok', views.UpdateOkFunc),
    path('delete/', views.DeleteFunc), 
]
