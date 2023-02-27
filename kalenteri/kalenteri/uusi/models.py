from django.db import models

class Kalenteri(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    
class Ohjelmasi(models.Model):
    pub_date = models.DateField()
    headLine = models.CharField(max_length=80)   
    content = models.TextField()
    reporter = models.ForeignKey(Kalenteri,
on_delete=models.CASCADE)

    def __str__(self):
        return self.headLine