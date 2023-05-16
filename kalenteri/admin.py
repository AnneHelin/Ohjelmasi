# Ladataan admin-tiedostoon tapahtumataulu
import datetime
from typing import Dict, Optional

from django.contrib import admin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Tapahtuma

@admin.register(Tapahtuma)
class TapahtumaAdmin(admin.ModelAdmin):
    list_display = ['paiva', 'alkamis_aika', 'loppu_aika', 'tarkenne']
    change_list_template = 'admin/tapahtuma/change_list.html'

    def change_view(self, request, extra_context=None):
        after_day = request.GET.get('paiva_gte', None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(vuosi=int(split_after_day[0]), kuukasi=int(split_after_day[1]), paiva=1)
            except:
                paiva = datetime.date.today()
                
        edellinen_kuukausi = datetime.date(vuosi=paiva.vuosi, kuukausi=paiva.kuukausi, paiva=1) # Applies for the first day of this month
        edellinen_kuukausi = edellinen_kuukausi - datetime.timedelta(days=1) # Backs up a single day 
        edellinen_kuukausi = datetime.date(vuosi=edellinen_kuukausi.vuosi, kuukausi=edellinen_kuukausi.kuukausi)# Retrieves the first day of the previous month  

        eilinen_paiva = kalenteri.kuukausirange(d.vuosi, d.kuukausi)
        seuraava_kuukausi = datetime.date(vuosi=d.vuosi, kuukausi=d.kuukausi, paiva=eilinen_paiva[1])
        seuraava_kuukausi = seuraava_kuukausi + datetime.timedelta(days=1) # The next day
        seuraava_kuukausi = datetime.date(vuosi=seuraava_kuukausi.vuosi, kuukausi=seuraava_kuukausi.kuukausi, paiva=1) # Searches for the first day of the following month

        extra_context['edellinen_kuukausi'] = reverse('admin:tapahtumat_tapahtuma_changelist') + '?päivä_gte=' + str(
            seuraava_kuukausi)
        extra_context['seuraava_kuukausi'] = reverse('admin:tapahtumat_tapahtuma_changelist') + '?päiv_gte=' + str(seuraava_kuukausi)

        kalenteri = Tapahtuma
        html_kalenteri = kalenteri.kuukausimuotoilu(paiva.vuosi, paiva.kuukausi, seuraava_vuosi= True)
        html_kalenteri = html_kalenteri('<td','<td width="170" height="170"')
        extra_context['kalenteri'] = mark_safe(html_kalenteri)
        return super(Tapahtuma, self).changelist_views(request,extra_context)







