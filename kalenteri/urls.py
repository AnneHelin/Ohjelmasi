from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from kalenteri import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.EtusivuView.as_view(), name='etusivu'),
    path('kirjautuminen/', views.kirjautuminen, name='kirjautuminen'),
    path('uloskirjautuminen/', views.uloskirjautuminen, name='uloskirjautuminen'),

    path('muokkaa-kayttajaa/', views.MuokkaaKayttajaaView.as_view(), name='muokkaa-kayttajaa'),
    path('vaihda-salasanaa//', views.VaihdaSalasanaaView.as_view(), name='vaihda-salasanaa'),

    path('hallinta/', views.HallistaView.as_view(), name='hallinta'), 
    path('lisaa-tapahtuma/', views.LisaaTapahtumaView.as_view(), name='lisaaminen')
    ]
