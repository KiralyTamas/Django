from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from clinicalApp.models import Patient
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from clinicalApp.forms import ClinicalForm


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
    
def addData(request,**kwargs):
    form=ClinicalForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    add_dict={'form':form,'patient':patient}
    if request.method=='POST':
        form=ClinicalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalApp/clinicalData.html',add_dict)