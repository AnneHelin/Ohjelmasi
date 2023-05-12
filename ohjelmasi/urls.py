"""ohjelmasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from ohjelmasi import views


from .views import index

urlpatterns = [
     path('admin/', admin.site.urls),

    path('', views.EtusivuView.as_view(), name='etusivu'),
    path('rekisteroityminen/', views.RekisteroityminenView.as_view(), name='rekisteroityminen'),
    path('kirjautuminen/', views.kirjautiminen, name='kirjautuminen'),
    path('uloskirjautuminen/', views.uloskirjautuminen, name='uloskirjautuminen'),

    path('vaihda-salasanaa/', views.VaihdaSalasanaaView.as_view(), name='vaihda-salasanaa'),

    path('hallinta/', views.HallintaView.as_view(), name='hallinta'),
    
    path('haku/', views.haku_tulokset, name='haku'),

    path('lisaa-tapahtuma/', views.LisaaTapahtumaView(), name='lisaaminen'),
    path('hallinta/muokkaa-tapahtumaa/<int:pk>/', views.MuokkaaTapahtumaaView.as_view(), name='muokkaaminen'),
    path('hallista/poista-tapahtuma/<int:pk>', views.PoistaTapahtumaView.as_view(), name='poistaminen'),
]   
#    path('', include('ohjelmasiapp.urls'))
   

  

  


    
   
 


