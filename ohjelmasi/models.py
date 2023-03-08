from django.db import models

class Kalenteri(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self. full_name
    
class Ohjelmasi(models.Model):  
    pub_date = models.DateField()
    headline = models.CharField(max_length=150)
    content = models.TextField()
    reporter = models.ForeignKey(on_delete=models.CASCADE)  

    def __str__(self):
        return self.headline