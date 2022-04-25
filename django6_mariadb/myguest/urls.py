from django.urls import path
from myguest import views

urlpatterns = [
    path('', views.ListFunc),
    path('Insert', views.InsertFunc),
    
]