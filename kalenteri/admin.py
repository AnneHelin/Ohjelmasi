from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Kategoria, ohjelmasi

class Kirjattufilter(SimpleListFilter):
    title = _('Merkattu')

    parameter_name = 'kirjattu'

    def lookups(self, request, model_admin):
        return(
            (None, "tieto")
            
        )

    def choices(self, cl):
        for (lookup, title) in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display':title,
            }

    def queryset(self, request, queryset):
        value = self.value()
        if value is None:
            return queryset.filter(merkitty=False)
        elif value == 'merktty'        

# Register your models here.