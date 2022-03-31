from django.shortcuts import render,redirect
from courseApp.models import Course
from courseApp.forms import CourseForm

def CourseList(request):
    courseList=Course.objects.all()
    course_dict={'course':courseList}
    return render(request,'courseApp/index.html',course_dict)

def AddCourse(request):
    form=CourseForm()
    course_dict={'form':form}
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'courseApp/addCourse.html',course_dict)

def UpdateCourse(request,id):
    course=Course.objects.get(id=id)
    form=CourseForm(instance=course)
    form_dict={'form':form,'Name':course.courseName}
    if request.method=='POST':
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'courseApp/updateCourse.html',form_dict)

def DeleteCourse(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('/')