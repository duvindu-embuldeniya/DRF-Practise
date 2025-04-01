from django.shortcuts import render, redirect
from . models import Project, Review, Tag, Profile, Skill
from . forms import ProjectForm, ProfileForm, UserRegistrationForm, SkillForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProfile, searchProject

from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def home(request): #render our profiles

    result = 2
    page = request.GET.get('page') if request.GET.get('page') else ''

    profiles, query = searchProfile(request)

    paginator = Paginator(profiles, result)

    try:
        profiles = paginator.page(page)

    except PageNotAnInteger as error1:
        page = '1'
        profiles = paginator.page(page)

    except EmptyPage as error2:
        page = paginator.num_pages
        profiles = paginator.page(page)        

    # query = request.GET.get('profile') if request.GET.get('profile') else ''
    # skills = request.GET.get('profile') if request.GET.get('profile') else ''
    
    # skills = Skill.objects.filter(
    #     Q(name__icontains = skills)
    # )
    
    # profiles = Profile.objects.distinct().filter(
    #     Q(name__icontains = query)|
    #     Q(user__skill__in = skills)
    # )

    context = {'profiles': profiles, 'query':query}
    return render(request, 'home/index.html', context)




def projects(request):

    page = request.GET.get('page') if request.GET.get('page') else ""
    result = 1

    projects, query = searchProject(request)

    paginator = Paginator(projects, result)

    try:
        projects = paginator.page(page)
    
    except PageNotAnInteger as error3:
        page = '1'
        projects = paginator.page(page)

    except EmptyPage as error4:
        page = paginator.num_pages
        projects = paginator.page(page)

    context = {'projects': projects, 'query': query}
    return render(request, 'home/projects.html', context)


def register(request):
    status = 'register'
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username =  new_user.username.lower()
            new_user.save()

            auth.login(request, new_user)
            messages.success(request, "Account created successfully!")
            return redirect('update-profile', username = new_user.username)
        else:
            messages.error(request, "Something went wrong!")
    context = {'status':status, 'form':form}
    return render(request, 'home/login_register.html', context)

 
def login(request):
    status = 'login'
    if request.user.is_authenticated:
        messages.info(request, 'You\'ve already loged-in!')
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = auth.authenticate(username = username, password = password)
        if auth_user is not None:
            auth.login(request, auth_user)
            messages.success(request, 'Successfully loged-in!')
            return redirect('home')
        else:
            messages.error(request, 'User doesn\'t exist!')
            return redirect('login')
    context = {'status':status}
    return render(request, 'home/login_register.html', context)


def logout(request):
    if not(request.user.is_authenticated):
        messages.info(request, 'You\'ve not loged-in!')
        return redirect('home')
    auth.logout(request)
    messages.success(request, 'Successfully loged-out!')
    return redirect('home')






def singleProfile(request, username):
    profile = User.objects.get(username = username).profile
    top_skills = profile.user.skill_set.exclude(description__exact = '')
    other_skills = profile.user.skill_set.filter(description__exact = '')
    projects = profile.user.project_set.all()
    context = {'profile':profile, 'top_skills': top_skills,
                'other_skills': other_skills, 'projects':projects}
    return render(request, 'home/profile.html', context)


def updateProfile(request, username):
    current_user = User.objects.get(username = username)
    current_profile = current_user.profile
    form = ProfileForm(instance = current_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance= current_profile)
        if form.is_valid():
            form.save()
            return redirect('single-profile', username = request.user.username)
    context = {'form':form}
    return render(request, 'home/profile_form.html', context)


def updateAccount(request, username):
    account_user = User.objects.get(username = username)
    context = {'account_user':account_user}
    return render(request, 'home/account.html', context)









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
        object.delete()
        return redirect('home')
    context = {'object':object}
    return render(request, 'home/delete_project.html', context)





def skillForm(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            new_skill = form.save(commit=False)
            new_skill.owner = request.user
            new_skill.save()
            messages.success(request, 'Skill added successfully')
            return redirect('update-account', username = request.user)
    context = {'form':form}
    return render(request, 'home/skill_form.html', context)


def skillUpdate(request, pk):
    skill = Skill.objects.get(id = pk)
    form = SkillForm(instance = skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully')
            return redirect('update-account', username = request.user)
    context = {'form':form}
    return render(request, 'home/skill_form.html', context)


def deleteSkill(request, pk):
    object = Skill.objects.get(id = pk)
    if request.method == 'POST':
        object.delete()
        messages.success(request, 'Skill deleted sucessfully')
        return redirect('update-account', username = request.user)
    context = {'object':object}
    return render(request, 'home/delete_object.html', context)