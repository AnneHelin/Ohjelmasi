from django.shortcuts import render
from django.http import HttpResponse

def ohjelmasi(request):
    return HttpResponse("Tervetuloa kalenteriin")