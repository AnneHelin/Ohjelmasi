import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Tapahtuma(models.Model):
    """
    Kirjaa tapahtuma.

    Tapahtuma merkitään kalenteriin, lisäämällä tieto "tapahtuma"-listaan."""

    nimi = models.CharField(max_length=100)
    lisätietoja = models.CharField(max_length=200)
    alku = models.DateTimeField()
    loppu = models.DateTimeField(null=True, blank=True)

    def __str__(self):
      alku = timezone.localtime(self.alku)
      loppu = timezone.localtime(self.loppu) if self.loppu else None
      return  f"{alku:%d.%m.%Y %H:%M} -- {loppu}"

       
