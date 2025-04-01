from django.db.models import Q
from . models import Profile, Project, Skill, Tag



def searchProfile(request):

    query = request.GET.get('profile') if request.GET.get('profile') else ''
    skills = Skill.objects.filter(
        Q(name__icontains = query)
    )

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = query) |
        Q(user__skill__in = skills) |
        Q(user__username__icontains = query)
    )
    return profiles, query



def searchProject(request):

    query = request.GET.get('project') if request.GET.get('project') else ''
    tags = Tag.objects.filter(
        Q(name__icontains = query)
    )

    projects = Project.objects.distinct().filter(
        Q(title__icontains = query)|
        Q(tags__in = tags)|
        Q(owner__username__icontains = query)
    )

    return projects, query