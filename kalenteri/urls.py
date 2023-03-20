from django.urls import path

from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # Tapahtuma
    path('<int:tapahtuma_id>/', views.tapahtuma, name='tapahtuma'),
    # Aika
    path('<int:aika_id>/', views.aloitusaika, name='aloitusaika'),
    
]