from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Tapahtuma

def index(request):
    return HttpResponse("Welcome, You're at the calendar index.")

def tapahtuma(request, tapahtuma_id):
    return HttpResponse("You're looking at tapahtuma%s." % tapahtuma_id)

def aloitusaika(request, aloitusaika_id):
    return HttpResponse("You're write start text%s." % aloitusaika_id) 

def index(request).
    lastest_tapahtuma_list = Tapahtuma.objects.order_by('aloitus_aia')[:6]
    template =
    loader.get_template('kalenteri/index.html')
    content = { 'latest_tapahtuma_list': lastest_tapahtuma_list,
        }
    return
HttpResponse    

def index(request):
    lastest_tapahtuma_list =
    tapahtuma.objects.order_by
    context = {'lastest_tapahtuma_list': lastest_tapahtuma_list}
    return render(request 'kalenteri/index.html', context)