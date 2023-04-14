from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import Tapahtuma
 

# Create your views here.


def tapahtuma(request):
    return render(request,'tapahtuma.html')

def image(request):
    return render(request, 'image.html')


def submitforum(request):
    return JsonResponse
