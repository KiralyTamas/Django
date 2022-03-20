from django.db import models

class Passenger(models.Model):
    firstName=models.CharField(max_length=40, verbose_name='Vezeték Név')
    lastName=models.CharField(max_length=40, verbose_name='Kereszt Név')
    email=models.EmailField(verbose_name='Email Cím')
    reward_point=models.IntegerField(verbose_name='Jutalom Pontok')