from django.db import models

class Employee(models.Model):
    firstName=models.CharField(max_length=40, verbose_name='Vezetéknév')
    lastName=models.CharField(max_length=40, verbose_name='Keresztnév')
    salary=models.FloatField(verbose_name='Fizetés')
    email=models.EmailField(verbose_name='Email cím')
    
    def __str__(self):
        return self.firstName+str(" ")+self.lastName