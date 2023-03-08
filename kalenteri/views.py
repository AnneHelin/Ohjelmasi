from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Tervetuloa kalenteriisi")
def merkkaus(request):
    return HttpResponse("Tervetuloa kalenteriisi")

#Functions gets entry from index.html's 
def entry_page(request, entry):
    name = entry        # Places the title
    print(f"checkin the title: {entry}")

    