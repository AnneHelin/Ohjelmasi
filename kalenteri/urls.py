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
        

        # path('', views.kalenteri, name="kalenteri"),
       # path('<int:year> / <str:month> / <str:day>', views.kalenteri, name='kalenteri'),
        
        # path('<int:year> / <str:month>/ / <str:day>', views.home, name="kalenteri"),
        ]       







