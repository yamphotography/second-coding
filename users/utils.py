from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from .models import *


def paginateProject(request, profileslist, results):
    
    page = request.GET.get('page')
    paginator = Paginator(profileslist, results)
  

    # projects = paginator.get_page(int(page))
    try:
        profileslist = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profileslist = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profileslist = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profileslist

def searchProfile(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skills = Skill.objects.filter(name__iexact=search_query)
    profileslist = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skills))

    return profileslist, search_query

# projects, search_query = searchProject(request)
#     custom_range, projects = paginateProject(request, projects, 6)
# {% include 'pagination.html' with queryset=projects custom_range=custom_range %}
# {% if queryset.has_other_pages %}
# def searchProject(request):
#     search_query = ''
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')
#     tags = Tag.objects.filter(name__iexact=search_query)
#     projects = Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query)| Q(owner__name__icontains=search_query) | Q(tags__in=tags))

#     return projects, search_query
