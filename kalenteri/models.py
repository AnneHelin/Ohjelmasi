import datetime
from django.db import models
from django.utils import timezone


class Kalenterisi(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self. full_name >= timezone.now() - datetime.timedelta(days=1)
    
class Kalenterisi(models.Model):  
    pub_date = models.DateField()
    headline = models.CharField(max_length=150)
    content = models.TextField()
    

    def __str__(self):
        return self.headline
    