from django.urls import path

from . import views

urlpatterns = [
    # index: /kalenteri/
    path('', views.index, name='index'),
    # index: /kalenteri/
    path('<int:teksti_id>/', views.detail, name='detail')
    
]