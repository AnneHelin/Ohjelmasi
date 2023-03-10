from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def ohjelmasi(request):
    return HttpResponse("Tervetuloa kalenteriin")

