from django.contrib import admin

from .models import ohjelmasi

@admin.register(ohjelmasi)
class OhjelmasiAdmin(admin.ModelAdmin):
    pass
