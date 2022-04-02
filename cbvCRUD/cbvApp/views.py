from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from cbvApp.models import Student

class StudentListView(ListView):
    model=Student
    # Alap html elérése az app-unkon belül van: templates/cbvApp/student_list.html
    # Alap objektum meghívási név: student_list
    # Elérési út átírható: template_name= 'cbvApp/index.html'
class StudentDetailView(DetailView):
    model=Student
    # Alap html elérése az app-unkon belül van: templates/cbvApp/student_detail.html
    # Alap objektum meghívási név: student
    # Elérési út átírható: template_name= 'cbvApp/detail.html'
        
class StudentCreateView(CreateView):
    model=Student
    fields=['firstName','lastName','testScore']
    # Alap html elérése az app-unkon belül van: templates/cbvApp/student_form.html
    # Elérési út átírható: template_name= 'cbvApp/create_form.html'
    
class StudentUpdateView(UpdateView):
    model=Student
    fields=['testScore']
    template_name='cbvApp/update.html'
    
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('students')
    # Alap html elérése az app-unkon belül van: templates/cbvApp/student_confirm_delete.html
    # Elérési út átírható: template_name= 'cbvApp/delete.html'