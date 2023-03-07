from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Tervetuloa kalenteriisi")
def merkkaus(request):
    return HttpResponse("Tervetuloa kalenteriisi")

