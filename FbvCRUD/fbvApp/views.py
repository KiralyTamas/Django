from django.shortcuts import redirect, render
from fbvApp.models import Student
from fbvApp.forms import StudentForm

def getStudent(request):
    students=Student.objects.all()
    students_dict={'students':students}
    return render(request, 'fbvApp/index.html',students_dict)

def createStudent(request):
    form=StudentForm()
    form_dict={'form':form}
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'fbvApp/create.html',form_dict)

def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def updateStudent(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    student_dict={'form':form}
    if request.method=='POST':
        print("1")
        form=StudentForm(request.POST,instance=student)
        print("2")
        if form.is_valid():
            print("3")
            form.save()
            return redirect('/')
    return render(request,'fbvApp/update.html',student_dict)