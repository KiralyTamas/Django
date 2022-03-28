from django.db import models

class Project(models.Model):
    startDate=models.DateField()
    endDate=models.DateField()
    name=models.CharField(max_length=80)
    assignedTo=models.CharField(max_length=80)
    priority=models.IntegerField()