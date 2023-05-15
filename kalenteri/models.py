from __future__ import unicode_literals

from django.db import models

# Luodaan tapahtumataulu

class Tapahtuma(models.Model):
    """
    Kirjaa tapahtuma.

    Tapahtuma merkitään kalenteriin, lisäämällä tieto "tapahtuma"-listaan."""
    # Lisätään taululle kentät
    otsikko = models.CharField(max_length=150)
    lisätieto = models.TextField()
    aloitus = models.DateTimeField()
    lopetus = models.DateTimeField()

    # Check overlap
    def check_overlap(self, korjattu_aloitus, korjattu_lopetus, seuraava_alku, seuraava_lopetus):
        samaan_aikaan = False
        if seuraava_alku == korjattu_lopetus or seuraava_lopetus == korjattu_aloitus:
          samaan_aikaan = False
        elif (seuraava_alku >= korjattu_aloitus and seuraava_alku <=korjattu_lopetus) or (seuraava_lopetus >= korjattu_aloitus and seuraava_lopetus <=seuraava_lopetus):
          samaan_aikaan = True
        elif seuraava_alku <= korjattu_aloitus and seuraava_lopetus >= korjattu_lopetus: 
          samaan_aikaan = True

          return samaan_aikaan

       
        