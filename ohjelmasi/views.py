from django.shortcuts import render
from django.http import HttpResponse
from . import views

def index(request):
    return HttpResponse('<h1>Tervetuloa kalenteriin</h1>')


def kalenteri(request):
    return render(request, 'index.html')

def kalenteri(request):
    return render(request, 'kirjautumissivu.html'),

def kalenteri(request):
    return render(request, "merkitsemissivu.html"),
 



