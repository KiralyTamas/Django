from django.shortcuts import render
from cbvCCApp.models import Course
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

class CourseList(ListView):
    model=Course
    template_name='cbvCCApp/index.html'
    
class CourseDetail(DetailView):
    model=Course
    template_name='cbvCCApp/detail.html'