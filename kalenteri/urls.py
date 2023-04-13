from django.urls import path
from . import views 
from django.http import HttpResponse, JsonResponse


urlpatterns = [
    path('', views.tapahtuma, name='tapahtuma'),
    path('tapahtuma', views.tapahtuma, name='tapahtuma'),
    path('forms', views.form, 'forms'),
    path('submitforum', views.submitforum, name='submitforum'),
]