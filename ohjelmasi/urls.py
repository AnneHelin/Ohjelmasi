from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('kalenteri', include('kalenteri.urls')),
    path('admin/', admin.site.urls),
]
