from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json
from .models import Project
from tasks.models import Task
from users.views import admin_required, authenticated_required

# Create your views here.

@require_http_methods(["GET"])
@authenticated_required
def ProjectListView(request):
    user_role = request.session.get('user_role') or getattr(request.user, 'role', None)
    
    if user_role == 'Admin':
        projects = Project.objects.all()
    else:
        user_assigned = request.session.get('username') or getattr(request.user, 'username', None)
        tasks = Task.objects.filter(user_assigned=user_assigned)
        project_ids = set(task.project_id for task in tasks)
        projects = Project.objects.filter(id__in=project_ids)
    
    projects_data = [
        {
            'id': project.id,
            'project_name': project.project_name,
            'project_description': project.project_description,
            'status': project.status,
            'hours_consumed': project.hours_consumed,
            'start_date': str(project.start_date),
            'end_date': str(project.end_date),
        }
        for project in projects
    ]
    return JsonResponse(projects_data, safe=False)

@require_http_methods(["GET"])
@authenticated_required
def ProjectDetailView(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    user_role = request.session.get('user_role') or getattr(request.user, 'role', None)
    if user_role != 'Admin':
        user_assigned = request.session.get('username') or getattr(request.user, 'username', None)
        if not Task.objects.filter(project=project, user_assigned=user_assigned).exists():
            return JsonResponse({'error': 'Access denied'}, status=403)
    
    project_data = {
        'id': project.id,
        'project_name': project.project_name,
        'project_description': project.project_description,
        'status': project.status,
        'hours_consumed': project.hours_consumed,
        'start_date': str(project.start_date),
        'end_date': str(project.end_date),
    }
    return JsonResponse(project_data)

@csrf_exempt
@require_http_methods(["POST"])
@admin_required
def ProjectCreateView(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    required_fields = ['project_name', 'project_description', 'hours_consumed', 'start_date', 'end_date']
    for field in required_fields:
        if field not in data:
            return JsonResponse({'error': f'Missing field: {field}'}, status=400)
    start_date = date.fromisoformat(data['start_date'])
    today = date.today()
    status = "IN PROGRESS" if start_date == today else "CREATED"
    
    try:
        project = Project.objects.create(
            project_name=data['project_name'],
            project_description=data['project_description'],
            status=status,
            hours_consumed=float(data['hours_consumed']),
            start_date=start_date,
            end_date=date.fromisoformat(data['end_date'])
        )
        
        return JsonResponse({
            'id': project.id,
            'project_name': project.project_name,
            'project_description': project.project_description,
            'status': project.status,
            'hours_consumed': project.hours_consumed,
            'start_date': str(project.start_date),
            'end_date': str(project.end_date),
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
