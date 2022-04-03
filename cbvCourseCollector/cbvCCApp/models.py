from django.db import models
from django.urls import reverse

class Course(models.Model):
    courseName=models.CharField(max_length=40,verbose_name='Tananyag Név')
    description=models.TextField(verbose_name='Tananyag Leírás')
    instructor=models.CharField(max_length=40, verbose_name='Tanár')
    rates=models.FloatField(verbose_name='Értékelés')
    
    def get_absolute_url(self):
        return reverse("index")
    