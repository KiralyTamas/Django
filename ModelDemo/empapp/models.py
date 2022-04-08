from django.db import models

class Employee(models.Model):
    firstName=models.CharField(max_length=40, verbose_name='Vezetéknév')
    lastName=models.CharField(max_length=40, verbose_name='Keresztnév')
    salary=models.FloatField(verbose_name='Fizetés')
    email=models.EmailField(verbose_name='Email cím')
    
    def __str__(self):
        return self.firstName+str(" ")+self.lastName

class Programmer(models.Model):
    name=models.CharField(max_length=40, verbose_name='Programozó Neve')
    salary=models.IntegerField()
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name=models.CharField(max_length=40)
    programmers=models.ManyToManyField(Programmer)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name=models.CharField(max_length=40)
    
class PhoneNumber(models.Model):
    typee=models.CharField(max_length=10)
    number=models.CharField(max_length=10)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
class Person(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    age=models.IntegerField()
    
class License(models.Model):
    typ=models.CharField(max_length=10)
    validFrom=models.DateField()
    validTo=models.DateField()
    person=models.OneToOneField(Person,on_delete=models.CASCADE)