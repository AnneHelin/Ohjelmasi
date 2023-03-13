from django.urls import path

from . import views

urlpatterns = [
    # ex: /kalenteri
    path('', views.Index, name='index'),      
       
]   
   
