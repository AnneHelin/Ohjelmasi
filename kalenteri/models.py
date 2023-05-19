from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime
# Luodaan tapahtumataulu

class Tapahtuma(models.Model):
    """
    Kirjaa tapahtuma.

    Tapahtuma merkitään kalenteriin, lisäämällä tieto "tapahtuma"-listaan."""
    # Lisätään taululle kentät
    otsikko = models.CharField(max_length=150)
    lisätieto = models.TextField(max_length=250)
    aloitusaika = models.DateTimeField()
    lopetusaika = models.DateTimeField()
    blank=True

    def __str__(self):
       aloitus =  timezone.localtime(self.aloitus)
       lopetus = timezone.localtime(self.lopetus) if self.lopetus else None

    # Check overlap
    def check_overlap(self, korjattu_aloitus, korjattu_lopetus, seuraava_alku, seuraava_lopetus):
        samaan_aikaan = False
        if seuraava_alku == korjattu_lopetus or seuraava_lopetus == korjattu_aloitus:
          samaan_aikaan = False
        elif (seuraava_alku >= korjattu_aloitus and seuraava_alku <=korjattu_lopetus) or (seuraava_lopetus >= korjattu_aloitus and seuraava_lopetus <=seuraava_lopetus):
          samaan_aikaan = True
        elif seuraava_alku <= korjattu_aloitus and seuraava_lopetus >= korjattu_lopetus: 
          samaan_aikaan = True

          return samaan_aikaan

    def get_absolute_url(self):
       url = reversed('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
       return u'<a href= "%s">%s</a>' % (url, str(self.aloitus_aika))
    
    def clean(self):
      if self.lopetus_aika <= self.aloitus_aika:
            raise ValueError('The end time must be later than the start time')
       
      ohjelma = ohjelma.object.filter(day=self.day)
      if ohjelma.exists():
         for ohjelma in ohjelma:
            if self.check_overlap(ohjelma.aloitus_aika, ohjelma.lopetus_aika, self.aloitus_aika, self.lopetus_aika):
              raise ValueError(
                 'There is overlap with another program: ' + str(ohjelma.paiva) + ',' + str(
                 ohjelma.aloitus_aika) + '-' + str(ohjelma.lopetus_aika))
                 

       
        