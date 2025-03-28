from django.shortcuts import render, redirect
from . models import Project, Review, Tag
from . forms import ProjectForm

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'home/index.html', context)

def singleProject(request, pk):
    project = Project.objects.get(id = pk)
    context = {'project':project}
    return render(request, 'home/single-project.html',context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_project = form.save()
            return redirect('single-project', pk=new_project.pk)
    context = {'form':form}
    return render(request, 'home/project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('single-project', pk=project.pk)
    context = {'form':form}
    return render(request, 'home/project_form.html', context)

def deleteProject(request, pk):
    object = Project.objects.get(id=pk)
    if request.method == 'POST':
        Project.delete()
        return redirect('home')
    context = {'object':object}
    return render(request, 'home/delete_object.html', context)