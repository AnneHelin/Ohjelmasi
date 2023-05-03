from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse



class Tapahtuma(models.Model):
    day = models.DateField(u'Päivän tapahtuma', help_text=u'päivän tapahtuma')
    start_time = models.TimeField(u'aloitusaika', help_text=u'alotusaika')
    end_time = models.TimeField(u'lopetuaika', help_text=u'lopetusaika', blank=True, null=True)
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Sijainti:
        verbose_name = u'Ohjelmasi'  # Headline
        verbose_name_plural = u'Ohjelmasi'

    def tarkistaa_tapahtuman(self, alkamis_aika, loppu_aika, uusi_alku, uusi_loppu):
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

            
    


