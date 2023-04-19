from datetime import datetime
from pkgutil import get_data
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Kalenteri


# Create your views here.

def index(request):
    return HttpResponse('Tervetuloa kalenteriisi')

class KalenteriView(generic.ListView):
    model = Kalenteri
    template_name = 'kalenteri/kalenteri.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Käytä tätä päivää
        day = get_data(self.request.GET.get('päivä', None))

        # Kalenteriluokan lisäys tälle vuodelle
        kalenteri= Kalenteri(day.year, day.month)

        # Kalenterin palautus taulukkona
        html_kalenteri= kalenteri.kuukausimuotoilu(withyear=True)
        context['kalenteri'] = mark_safe(html_kalenteri)
        return context
    
def get_day(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)   
    return datetime.today()
 

 