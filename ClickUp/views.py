from django import tasks
from django.shortcuts import render
from django.http import JsonResponse

def getRoutes(request):
    return JsonResponse([
        'GET /api/clickup/tasks/',
        'GET /api/clickup/tasks/<task_id>/',
        'POST /api/clickup/tasks/',
    ], safe=False)

def getTasks(request):
    tasks = tasks.get_all_tasks()
    return JsonResponse(tasks, safe=False)
