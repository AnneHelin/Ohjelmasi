from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Tervetuloa kalenteriisi")
def merkkaus(request):
    return HttpResponse("Tervetuloa kalenteriisi")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

