from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Enter the app

    # path('', include("kalenteri.app"))
]