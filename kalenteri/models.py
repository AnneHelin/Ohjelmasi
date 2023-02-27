import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy 


class Ohjelmasi(models.Model):
    """
    Merkitty

    Kerrottu tapahtuma
    """
    tapahtuma = models.CharField(max_length=75)
    alku = models.DateField()
    

    