from django.urls import path
from . import views




urlpatterns = [
        # path converters
        # int: numbers
        # str: string
        # path: whole urls/
        # slug: hyphen-and_underscores_stuff
        # UUID: universally unique idemtifier
        # path('', views.index, name='index'),
        path("" , views.index, name="index"),
        path("<int:year_id/", views.etusivu, name='etusivu'),
        path("<int:month_id/", views.etusivu, name='etusivu'),
        path("<int:day_id/", views.day, name='day'),
        path('<request/', views.kirjaa_ohjelmasi, name='kirjaa_ohjelmasi'),

        # path('', views.kalenteri, name="kalenteri"),
       # path('<int:year> / <str:month> / <str:day>', views.kalenteri, name='kalenteri'),
        
        # path('<int:year> / <str:month>/ / <str:day>', views.home, name="kalenteri"),
        ]       







