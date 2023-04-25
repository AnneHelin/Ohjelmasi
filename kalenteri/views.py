from django.http import( 
    HttpResponse, 
    HttpResponseBadRequest, 
    HttpResponseNotFound
)    
from django.shortcuts import render

from .models import Kalenteri

def kalenteri(request):
    "Tervetuloa kalenteriin!"
    return render(request,'index.html')

def kalenteri(request year, month):
    
