from django.shortcuts import render
from .models import Skills


def index(requests):
    project_serial = Skills.objects.all()
    return render(requests, 'skills/index.html', {'project_serial': project_serial})

