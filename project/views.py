from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def ProjectListView (request):
    return render(request, 'project/project_list.html')

def ProjectDetailView (request, pk):
    return render(request, 'project/project_detail.html', {'pk': pk})

def ProjectCreateView (request):
    return render(request, 'project/project_form.html')

