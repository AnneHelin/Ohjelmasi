from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.admin import SimpleListFilter



class Kirjattufilter(SimpleListFilter):
    title = _('Merkattu')

    parameter_name = 'kirjattu'

    def lookups(self, request, model_admin):
        return(
            (None, "tieto")
        )
    

# Register your models here.