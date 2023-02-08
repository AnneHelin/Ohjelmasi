from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('ohjelmasi/', include('ohjelmasi.urls')),
    path('admin/', admin.site.urls),
]