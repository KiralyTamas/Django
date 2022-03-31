from django.shortcuts import render
from django.views.generic import ListView,DetailView
from cbvApp.models import Student

class StudentListView(ListView):
    model=Student
    
class StudentDeatilView(DetailView):
    model=Student