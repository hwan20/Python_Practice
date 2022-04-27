from django.urls import path
from mysurvey import views

urlpatterns = [
    path('survey', views.surveyView),
    path('surveyprocess', views.surveyprocess),
    path('surveyshow', views.dataAnalysis),
]