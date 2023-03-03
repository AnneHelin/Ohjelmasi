from django.db import models
from django.utils import timesince
import datetime

class Kalenteri(models.Model):
    day = models.DateField(max_length=5)
    text = models.CharField(max_length=50)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Kalenteri,
on_delete=models.CASCADE)
models.CharField(max_length=30)

class Text(models.Model):
    #
    def __str__(self):
        return self.text_text
    
