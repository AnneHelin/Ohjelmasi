from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('kalenteri', include('kalenteri.urls')),
    path('admin/', admin.site.urls),
    path('', include("encyclopedia.urls")),
]

handler404 = "encyclopedia.views.error_404"
