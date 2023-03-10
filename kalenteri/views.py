from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import Question

def index(request):
    return HttpResponse("Tervetuloa kalenteriisi")
def merkkaus(request):
    return HttpResponse("Tervetuloa kalenteriisi")

#Functions gets entry from index.html's 
def entry_page(request, entry):
    name = entry        # Places the title
    print(f"checkin the title: {entry}")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id) 

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)   

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'kalenteri/detail.html', {'question':question})    

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)