from django import tasks
from django.shortcuts import render
from django.http import JsonResponse

def getRoutes(request):
    return JsonResponse([
        'GET /api/clickup/tasks/',
        'GET /api/clickup/tasks/<task_id>/',
        'POST /api/clickup/tasks/',
    ], safe=False)

def ClickUpTaskListView(request):
    return JsonResponse({'message': 'List of ClickUp tasks'})

def ClickUpTaskDetailView(request, task_id):
    return JsonResponse({'message': f'Details of ClickUp task {task_id}'})

def ClickUpTaskCreateView(request):
    return JsonResponse({'message': 'Create a new ClickUp task'})

