from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from users.decorators import admin_required

# Create your views here.
@admin_required
def ProjectListView (request):
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})



def ProjectDetailView (request, pk):
    return render(request, 'project/project_detail.html', {'pk': pk})

def ProjectCreateView (request):
    return render(request, 'project/project_form.html')

