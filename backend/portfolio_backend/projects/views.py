from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def home(request):
    return render(request, 'projects/home.html')