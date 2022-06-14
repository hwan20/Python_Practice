from django.urls import path
from myboard.views import view1

urlpatterns = [
    #myboard 앱에 들어오는 요청은 다 여기에서 처리
    #경로 요청이 많을 경우 views대신에 사용할 폴더를 생성하고 거기에 경로를 줄 수도 있다
    #너무 복잡해 지니 같은 성격끼리 묶음
    path('list', view1.listFunc),
    
    path('insert', view1.insertFunc),
    path('insertok', view1.insertOkFunc),
    
    path('search', view1.searchFunc),
    
    path('content', view1.contentFunc),
    
    path('update', view1.updateFunc),
    path('updateok', view1.updateOkFunc),
    
    path('delete', view1.deleteFunc),
    path('deleteok', view1.deleteOkFunc),
    
]
