from __future__ import unicode_literals

from django.db import models

class Tapahtuma(models.Model):
    day = models.DateField(u'Päivän tapahtuma', help_text=u'päivän tapahtuma')
    start_time = models.TimeField(u'aloitusaika', help_text=u'alotusaika')
    end_time = models.TimeField(u'lopetuaika', help_text=u'lopetusaika', blank=True, null=True)
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Sijainti:
        verbose_name = u'Ohjelmasi'  # Headline
        verbose_name_plural = u'Ohjelmasi'




