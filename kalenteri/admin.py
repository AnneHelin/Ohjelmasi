# -*- codin: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Ohjelmasi
import datetime
import kalenteri
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

# Your models register here

class OhjelmasiAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']
    change_form_template = 'admin/ohjelmasi/change_list.html'

    def changelist_view(self, request, extra_context=None):
        after_day = request.GET.get('day_gte', None)
        extra_context = extra_context or {}

        if not after_day:
            day = datetime.date.today()
        else:
            try:    
                split_after_day = after_day.split('-')
                day = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                day = datetime.date.today()

        previous_month = datetime.date(year=day.year, month=day.month, day=1) # Applies for the first day of this month
        previous_month = previous_month - datetime.timedelta(days=1) # Save each day separately
        previous_month = datetime.date(year=previous_month, month=previous_month.month, day=1) # Applies on the first day of the following month

        last_day = kalenteri.monthrange(day.year, day.month)
        next_month = datetime.date(year=day.year, month=day.month, day=last_day[1]) # Search for the last day of the current month
        next_month = next_month + datetime.timedelta(days=1) # The next day
        next_month = datetime.date(year=next_month.year, month=next_month.month, day=1) # Apply for the first day of the month

        extra_context['prevesious_month'] = reverse('admin:kalenteri_kalenteri_listamuutos') + '?day_gte=' + str(previous_month)
        extra_context['next_month'] = reverse('admin:kalenteri_kalenteri_listamuutos') +'?day_gte=' + str(next_month)

        cal = kalenteri()
        html_kalenteri = cal.formatmonth(day.year, day.month, withyear=True)
        html_kalenteri = html_kalenteri.replace('<td', '<td width="150" height="150"')
        extra_context['kalenteri'] = mark_safe(html_kalenteri)
        return super(KalenteriAdmin, self).changelist_view(request, extra_context)
    
admin.site.register(kalenteri, kalenteriadmin)    
