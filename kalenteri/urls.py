from django.urls import path
from . import views
from django.http import HttpResponse, JsonResponse


urlpatterns = [
    path('', views.Tapahtuma, name='tapahtuma'),
    path('tapahtuma', views.Tapahtuma, name='ohjelmasi'),
]







