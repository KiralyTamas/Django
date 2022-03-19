from django.shortcuts import render
from empapp.models import Employee

def employeedata(request):
    employees=Employee.objects.all()
    empDict={'employees':employees}
    return render(request,'empapp/employees.html',empDict)