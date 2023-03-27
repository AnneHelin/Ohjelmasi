from django.http import HttpResponse
from django.shortcuts import render

from .models import Tapahtuma
 

# Create your views here.

def index(request):
   return HttpResponse("Tervetuloa!")

def kalenteri(request):
   ohjelma = Tapahtuma.objects.all()
   context = {
       'ohjelma': ohjelma, 
   }
   return render(request, 'listaus.html', context)

def add(request_id):
   ohjelma = Tapahtuma.objects.get(id=id)