from django.shortcuts import render
from django.urls import reverse_lazy
from clinicalApp.models import Patient
from django.views.generic import ListView,CreateView,UpdateView,DeleteView


class PatientListView(ListView):
    model=Patient
    template_name='clinicalApp/index.html'
    
class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')
    template_name='clinicalApp/create.html'
    
class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')
    template_name='clinicalApp/update.html'
    
class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')
    template_name='clinicalApp/delete.html'