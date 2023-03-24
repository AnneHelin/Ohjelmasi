from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

 

# Create your views here.
def ohjelmasi(request):
    return HttpResponse('Tervetuloa kalenteriin')

def ohjelmasi(request):
    return HttpResponse('Teksti')

def index(request):
    return render(request, 'index.html')