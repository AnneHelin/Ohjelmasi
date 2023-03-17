from django.http import HttpResponse
from django.template import loader
from .models import Kalenterisi

def Index(request):
    return HttpResponse("Hello! Welcomen, to your calendar")




