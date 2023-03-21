import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Tapahtuma(models.Model):
    """¨
    Merkitse tapahtuma.
    Kirjaat sähköisesti allakkasi. Kirjaat mihin olet menossa ja kellonaika
    """
    otsikko = models.CharField(max_length=150)
    taphtuma = models.TextField(blank=True)
    aloitusaika = models.DateField()
    lisätieto = models.TextField(blank=True)

    
    def __str__(self):
        return self.taphtuma
    