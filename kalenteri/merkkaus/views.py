from django.shortcuts import render
from django.http import HttpResponse

def merkkaus(request):
    kalenteri = ('merkkaus.html')
    return HttpResponse("Tervetuloa kalenteriisi")

