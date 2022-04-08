from django.db import models

class Patient(models.Model):
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    age=models.IntegerField()
    
class ClinicalData(models.Model):
    COMPONENT_NAME=[('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName=models.CharField(choices=COMPONENT_NAME, max_length=20)
    componentValue=models.CharField(max_length=20)
    measuredDataTime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)