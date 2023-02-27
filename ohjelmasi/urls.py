from django.urls import path

from .views import kirjattu ohjelmasi



urlpatterns = [
    path('', kalenteri, name="ohjelmasi"),
    path('ohjelmasi/<int:id/', merkitty_ohjelmasi, name="merkitty"),
]




