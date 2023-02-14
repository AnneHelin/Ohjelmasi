import datetime

from django.db import models
from django.utils import timezone
 

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    Question = models.ForeignKey(Question,
on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)

class Question(models.Model):
    #...
    def __str__(self):
        return self.entry_text

class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
        
class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
datetime.timedelta(days=1)