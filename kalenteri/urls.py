from django.urls import path
from . import views

urlpatterns = [
    path('', views.ohjelmasi, name='index'),
    path('teksti', views.ohjelmasi, name='teksti'),
    path('add/<int:a>/<int:b>', views.add, name='add'),
    path('')
]
    
