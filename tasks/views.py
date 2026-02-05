from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json
from .models import Task
from project.models import Project
from users.views import admin_or_manager_required

# Create your views here.

@require_http_methods(["POST"])
@admin_or_manager_required
@csrf_exempt
def TaskCreateView(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    required_fields = ['project', 'task_name', 'task_description', 'hours_consumed', 'user_assigned', 'start_date', 'end_date']
    for field in required_fields:
        if field not in data:
            return JsonResponse({'error': f'Missing field: {field}'}, status=400)

    try:
        project = Project.objects.get(id=data['project'])
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    
    start_date = date.fromisoformat(data['start_date'])
    today = date.today()
    status = "IN PROGRESS" if start_date == today else "CREATED"
    
    try:
        task = Task.objects.create(
            project=project,
            task_name=data['task_name'],
            task_description=data['task_description'],
            status=status,
            hours_consumed=float(data['hours_consumed']),
            user_assigned=data['user_assigned'],
            start_date=start_date,
            end_date=date.fromisoformat(data['end_date'])
        )
        
        return JsonResponse({
            'id': task.id,
            'project': task.project.id,
            'task_name': task.task_name,
            'task_description': task.task_description,
            'status': task.status,
            'hours_consumed': task.hours_consumed,
            'user_assigned': task.user_assigned,
            'start_date': str(task.start_date),
            'end_date': str(task.end_date),
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def TaskListView(request):
    tasks = Task.objects.all()
    tasks_data = [
        {
            'id': task.id,
            'project': task.project.id,
            'task_name': task.task_name,
            'task_description': task.task_description,
            'status': task.status,
            'hours_consumed': task.hours_consumed,
            'user_assigned': task.user_assigned,
            'start_date': str(task.start_date),
            'end_date': str(task.end_date),
        }
        for task in tasks
    ]
    return JsonResponse(tasks_data, safe=False)

def TaskDetailView(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
    
    task_data = {
        'id': task.id,
        'project': task.project.id,
        'task_name': task.task_name,
        'task_description': task.task_description,
        'status': task.status,
        'hours_consumed': task.hours_consumed,
        'user_assigned': task.user_assigned,
        'start_date': str(task.start_date),
        'end_date': str(task.end_date),
    }
    return JsonResponse(task_data)
