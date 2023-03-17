from django.db import models
from django.utils import timezone
import datetime

class Day(models.Model):
    date = models.DateField(max_length=5),
    clock_time = models.DateTimeField(max_length=10),
    entry_text = models.CharField(max_length=70)
    
def __str__(self):
    return self.day_field 