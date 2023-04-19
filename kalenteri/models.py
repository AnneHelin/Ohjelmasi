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

       
