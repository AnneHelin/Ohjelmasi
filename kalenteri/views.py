from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def kalenteri(request):
    return HttpResponse("Tervetuloa omaan kalenteriisi")

