from django.shortcuts import render, redirect
from .import models

# Create your views here.
def home(request):
    skills= models.Skill.objects.all()
    projects= models.Project.objects.all()
    contacts= models.Contact.objects.all()
    
    return render(request, 'index.html', {'skills': skills, 'projects': projects, 'contacts':contacts})