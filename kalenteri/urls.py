from django.urls import path
from . import views 
from django.http import HttpResponse, JsonResponse


urlpatterns = [
    # Path Converters
    # int: numbers
    # str : strings
    # path: whole urls/
    # slug: hyphen_and_underscores_stuff
    # UUID: universally unique identifier
    path('', views.tapahtuma, name='tapahtuma'),
    path('tapahtuma', views.tapahtuma, name='tapahtuma'),
    #path('submitforum', views.submitforum, name='submitforum'),
    path('<int:year>/<str:month>', views.tapahtuma)
]







