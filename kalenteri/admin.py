# Ladataan admin-tiedostoon tapahtumataulu
from django.contrib import admin
from .models import Tapahtuma

# Yhdistetään Tapahtuma-taulu ja admin
@admin.register(Tapahtuma)
class TapahtumaAdmin(admin.ModelAdmin):
    pass



