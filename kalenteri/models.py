from django.db import models
from django.utils import timezone
import datetime

from . import models

class Tapahtuma(models.Model):
    taphtuma = models.Tapahtuma(max_lenght=70)
    aloitusaika = models.datetime()

    
    def __str__(self):
        return self.taphtuma
    

    


