from django.urls import path
from . import views 
from django.http import HttpResponse, JsonResponse

urlpatterns = [
    path('', views.kalenteri, name='index'),
    path('tapahtuma', views.tapahtuma, name='tapahtuma'),
    path('aloitusaika', views.aloitusaika, name='aloitusaika'),
    path('lisatiedot', views.lisatiedot, name='lisatiedot'),
    path('form', views.form,name='form'),
]