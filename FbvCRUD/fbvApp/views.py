from django.shortcuts import redirect, render
from fbvApp.models import Student
from fbvApp.forms import StudentForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def getStudent(request):
    students=Student.objects.all()
    students_dict={'students':students}
    return render(request, 'fbvApp/index.html',students_dict)

@login_required
def createStudent(request):
    form=StudentForm()
    form_dict={'form':form}
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'fbvApp/create.html',form_dict)

@login_required
@permission_required('fbvApp.delete_student')
def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')

@login_required
def updateStudent(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    student_dict={'form':form}
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'fbvApp/update.html',student_dict)


def logout(request):
    return render(request, 'fbvApp/logout.html')