from django.urls import path
from . import views

urlpatterns = [
    path('merkkaus/', views.merkkaus, name='merkkaus'),
]