from django.shortcuts import render
from django.http import HttpResponse

def ohjelmasi(request):
    return HttpResponse("Tervetuloa kalenteriin")

def error_404(request, exception):
    context = {}
    response = render(request, 'encyclopedia/error_404.html', context=context)
    response.status_code = 404
    return response