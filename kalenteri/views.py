from django.shortcuts import render
from django.http import HttpResponse

def merkkaus(request):
    return HttpResponse("Tervetuloa kalenteriisi")


