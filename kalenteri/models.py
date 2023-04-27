from datetime import timedelta
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save,pre_save
# from apps.ohjelmasi.models import ohjelmasi

# Luodaan tapahtumataulu

class Tapahtuma(models.Model):
    """
    Kirjaa tapahtuma.

    Tapahtuma merkitään kalenteriin, lisäämällä tieto "tapahtuma"-listaan."""
    # Lisätään taululle kentät
    id = models.AutoField(primary_key= True)
    nimi = models.CharField(max_length = 500, blank = False, null = False)
    kuvaus = models.TextField(max_length = 200, blank = False,null= False)
    päivämäärän_luonti = models.DateField('päivämäärä', auto_now = True, auto_now_add= False)
    käyttäjä = models.CharField(max_length= 100, blank = False, null = False)
    päivien_määrä = models. SmallIntegerField('päivien määrä', auto_created= 7) 
    def perinteinen_avain(self):
        return f'{self.nimi} {self.app}'
    class Meta:
        monisanainen_nimi = 'Kirjoittaja'
        monikko_sanat = 'Kirjoittajat'
        tekijä =  ['Nmi']

  
    def __str__(self):
        return self.nimi
    
    def osa_tekijä(self):
        tekija = str([kirjoittaja for kirjoittaja in self.kirjoittaaja_id.all().values_list('nimi', flat = True)]).replace("[","").replace("]","")
        return tekija
    
class merkitseminen(models.Model):
    """Mallien määrittely"""
    # TODO: Kenttien määrittely
    id = models.AutoField(primary_key= True)
    nimi = models.CharField
    kuvaus = models.CharField
    käyttäja = models.ForeignKey( on_delete=models.CASCADE)
    päivien_määrä = models.SmallIntegerField('Viikonpäivien määrä',default= 7)
    luonti_päivä = models.DateField('Luontipäivä', auto_now = True, auto_now_add = False)
    


    class Päämäärä:
        """Kirjauksien määrittely."""

        moniosainen_nimi = 'Kirjaus'
        





        

   