from django.db import models

class Course(models.Model):
    courseName=models.CharField(max_length=40,verbose_name='Tananyag Név')
    description=models.TextField(verbose_name='Tananyag Leírás')
    rates=models.FloatField(verbose_name='Értékelés')