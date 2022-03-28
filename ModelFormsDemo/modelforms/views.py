from django.shortcuts import render
from modelforms.models import Project
from modelforms.forms import ProjectForm
from modelforms.models import Project

def index(request):
    return render(request, 'modelforms/index.html')

def listProjects(request):
    projectsList=Project.objects.all()
    projects_dict={'projects':projectsList}
    return render(request, 'modelforms/listProjects.html',projects_dict)

def addProject(request):
    form=ProjectForm()
    form_dict={'form':form}
    if form.methot=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'modelforms/addProjects.html',form_dict)