from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db.models import Model

# import datetime
import datetime

# creating an instance of

# datetime.date


class Tapahtuma(models.Model):
    tapahtuma_id = models.AutoField(primary_key=True)
    tapahtuma_nimi = models.CharField(max_length=150,null=True,blank=True)
    alkamin_paiva = models.DateTimeField(null=True,blank=True)
    paattymis_paiva = models.DateTimeField(null=True,blank=True)
    tapahtuma_tyyppi = models.CharField(max_length=20,name=True,blank=True)

    def __str__(self):
        return self.tapahtuma_nimi
    
   # def tarkistaa_tapahtuman(self, alkamis_aika, loppu_aika, uusi_alku, uusi_loppu):
        samanaikainen = False
        if uusi_alku == loppu_aika or uusi_alku == loppu_aika:
            samanaikainen = False
        elif (uusi_alku >= loppu_aika and uusi_alku <= loppu_aika) or (uusi_loppu >= alkamis_aika and uusi_loppu <= loppu_aika):
            samanaikainen = True
        elif uusi_alku <= loppu_aika and uusi_loppu >= loppu_aika <= loppu_aika:

            return samanaikainen
    
    def  get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%S">%s</a>' % (url, str(self.start_time))
    
    def clean(self):
        if self.loppu_aika <= self.alkamis_aika:
            raise ValidationError('Aloitusaika ennen päättymisaikaa')
        
        kalenteri = kalenteri.objects.filter(days=self.day)
        if kalenteri.exists():
            for kalenteri in kalenteri:
                if self.tarkistaa_tapahtuman(kalenteri.alkamis_aika, kalenteri.loppu_aika, self.alkamis_aika, self.loppu_aika):
                    raise ValidationError('Useampi tapahtuma samaan aikaan:' + str(Tapahtuma.day) + ',' + str(Tapahtuma.alkamis_aika) + '-' + str(Tapahtuma.loppu_aika))

            
    


