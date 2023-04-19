
from django.conf.urls import url
from . import views 
from django.http import HttpResponse, JsonResponse

app_name = 'kalenteri'

urlpatterns = [
        url('index', views.index, name='index'),

]







