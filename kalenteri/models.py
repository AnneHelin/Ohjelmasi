import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Luodaan tapahtumataulu

class Tapahtuma(models.Model):
    """
    Kirjaa tapahtuma.

    Tapahtuma merkitään kalenteriin, lisäämällä tieto "tapahtuma"-listaan."""
    # Lisätään taululle kentät
    otsikko = models.CharField(max_length=150)
    lisätieto = models.TextField()
    aloitus = models.DateTimeField()
    lopetus = models.DateTimeField()
    


    def __str__(self):
      alku = timezone.localtime(self.alku)
      loppu = timezone.localtime(self.loppu) if self.loppu else None
      return  f"{alku:%d.%m.%Y %H:%M} -- {loppu}"


    
    def kirjaa(self, user):
       """Kirjataan tapahtuma
       Palauttaa Truen, jos tapahtuman kirjaus onnistui"""

       if user in self.merkitty.all():
          return True
       merkitty = self.merkitty.all().count()
       if merkitty + 1 > self.tapahtuma:
          return False
       self.merkitty.add(user)
       return True

    def poista_merkkaus(self, user):
       if not self.onko_merkattu(user):
            return
       self.merkitty.remove(user)

    @property
    def onko_tilaa(self):
       return self.merkattu < self.Tapahtuma
    
    @property
    def kirjattu(self):
       return self.merkkaus.count()