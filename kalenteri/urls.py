from django.urls import path
from . import views 
from django.http import HttpResponse, JsonResponse

urlpatterns = [
    path('', views.kalenteri, name='index'),
    path('tapahtuma', views.tapahtuma, name='tapahtuma'),
    
]