from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import Tapahtuma
import kalenteri

 

# Create your views here.


def tapahtuma(request, year, month):
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(kalenteri.month_name).index(month)    
    month_number = int(month_number)

    # create a calendar

    
 