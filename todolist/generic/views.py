from dataclasses import field
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Project

# Create your views here.
class AddProject(CreateView):
    model = Project
    fields = ['project_name','project_description']
    template_name = 'generic/add.html'
    success_url = '/generic/view/'

