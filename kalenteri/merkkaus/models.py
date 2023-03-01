from django.db import models

class Merkkaus(models.Model):
    day = models.CharField(max_length=50)
    text = models.CharField(max_length=100)

    