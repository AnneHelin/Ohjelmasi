from django.urls import path
from . import views
from django.http import HttpResponse, JsonResponse

urlpatterns = [
    path('', views.index, name= "index"),
    path('kalenteri', views.kalenteri, name= "kalenteri"),
    path('add/<int:etusivu>/<int:merkitsemissivu>',views.add, name= "add"),
    

]
    
