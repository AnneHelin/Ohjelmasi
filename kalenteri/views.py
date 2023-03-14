from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Kalenterisi
def Index(request):
    return HttpResponse("Hello! Welcomen, to your calendar")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(reguest, question_id):
    reponse = "You're looking at the results of question %s."
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Kalenterisi.objects.order_by('-pub_date')[:5]
    output = ','.join([q.kalenteri_text for q in latest_question_list])
    return HttpResponse(output)


