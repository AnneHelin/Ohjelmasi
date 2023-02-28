import datetime

from django.db import models
from django.utils import timezone



class Ohjelmasi(models.Model):
    """
    Merkitty

    Kerrottu tapahtuma
    """
    tapahtuma = models.CharField(max_length=75)
    alku = models.DateField()
    tapahtuma_päivä = models.DateField(null=True)

    