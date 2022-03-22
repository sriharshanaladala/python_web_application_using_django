from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectsForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'myapp/projects.html', context)
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'myapp/single-project.html', {'project': projectObj})

def createProject(request):
    form = ProjectsForm()
    context = {'form': form}
    return render(request, "myapp/project_form.html", context)