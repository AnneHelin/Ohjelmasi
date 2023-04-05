from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import Tapahtuma
 

# Create your views here.
def kalenteri(request):
    return render(request, 'kalenteri.html')

def tapahtuma(request):
    return render(request,'tapahtuma.html')

def kalenteri(request):
    return render(request,'aloitusaika.html')

def kalenteri(request):
    return render(request,'lisätiedot.html')

def kalenteri(request):
    return render(request,'form.html')