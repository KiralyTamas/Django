from django.db import models

class Course(models.Model):
    courseName=models.CharField(max_length=40,verbose_name='Tananyag Név')
    description=models.TextField(verbose_name='Tananyag Leírás')
    instructor=models.CharField(default='', max_length=40, verbose_name='Tanár')
    rates=models.FloatField(verbose_name='Értékelés')