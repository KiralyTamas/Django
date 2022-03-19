from django.db import models

class Employee(models.Model):
    firstName=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    salary=models.FloatField()
    email=models.EmailField()