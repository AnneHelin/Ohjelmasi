from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

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

def kalentreri(request):
   return render(request, 'kalenteri.html')

def kalenteri(request, tapahtuma_id):
   try:
      tapahtuma = Tapahtuma.objects.get(pk=tapahtuma_id)
   except Tapahtuma.DoesNotExist:
      raise Http404("Tapahtumia ei tällä sivulla")
   return render(request, 'kalenteri/kalenteri.html', {'tapahtuma': tapahtuma})   

def kalenteri(request):
   return render(request, 'index.html')