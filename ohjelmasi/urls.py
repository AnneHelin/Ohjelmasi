from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404
from . import views
from .models import Question

urlpatterns = [
    path('kalenteri', include('kalenteri.urls')),
    path('admin/', admin.site.urls),
   
]


