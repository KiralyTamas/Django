from django.shortcuts import render
from fbvApp.models import Student

def getStudent(request):
    students=Student.objects.all()
    students_dict={'students':students}
    return render(request, 'fbvApp/index.html',students_dict)