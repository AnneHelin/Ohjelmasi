from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Kalenteri/', include('kalenteri.urls')),
    path('admin/' , admin.site.urls),
]


