from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("Tervetuloa omaan kalenteriisi")

