from django.http import HttpResponse

def index(requesr):
    return HttpResponse("Tervetuloa kalenteriisi")
