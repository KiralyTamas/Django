from cbvCCApp.models import Course
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

class CourseList(ListView):
    model=Course
    template_name='cbvCCApp/index.html'
    
class CourseDetail(DetailView):
    model=Course
    template_name='cbvCCApp/detail.html'
    
class CourseUpdate(UpdateView):
    model=Course
    fields=['courseName','description','instructor','rates']
    template_name='cbvCCApp/update.html'
    
class CourseDelete(DeleteView):
    model=Course
    template_name='cbvCCApp/delete.html'
    success_url=reverse_lazy('index')
    
class CourseCreate(CreateView):
    model=Course
    fields=['courseName','description','instructor','rates']
    template_name='cbvCCApp/create.html'