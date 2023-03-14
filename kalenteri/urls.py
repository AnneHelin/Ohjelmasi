from django.urls import path

from . import views

urlpatterns = [
    # ex: /kalenteri
    path('', views.Index, name='index'),      
    # ex: /kelenteri/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /kalenteri/5/results/
    path('<int:question_id>/results', views.results, name='results'),
    # ex: /kalenteri/5/votel/
    path('<int:question_id/vote/', views.vote, name='vote'),
       
]   
   
