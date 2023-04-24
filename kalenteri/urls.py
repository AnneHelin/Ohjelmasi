from django.urls import path
from . import views
from django.http import HttpResponse, JsonResponse


urlpatterns = [
        # Path Converters
        # int: numbers
        # str: tring
        # path: whole urls/
        # slug: hyphen-and_underscores_stuff
        # UUID: universally unique identifer
        #path(', views.tervetuloa, name="tervetuloa"),
        path('<int:year>/<str:month>/', views.kalenteri, name="kalenteri"),
        ]







