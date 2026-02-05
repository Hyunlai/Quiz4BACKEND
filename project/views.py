from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date
from .models import Project
from .serializers import ProjectSerializer
from tasks.models import Task


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        """Filter projects based on user role"""
        user_role = self.request.session.get('user_role') or getattr(self.request.user, 'role', None)
        
        if user_role == 'Admin':
            return Project.objects.all()
        else:
            user_assigned = self.request.session.get('username') or getattr(self.request.user, 'username', None)
            tasks = Task.objects.filter(user_assigned=user_assigned)
            project_ids = set(task.project_id for task in tasks)
            return Project.objects.filter(id__in=project_ids)
    
    def perform_create(self, serializer):
        """Auto-set status based on start_date"""
        start_date = serializer.validated_data.get('start_date')
        status_value = "IN PROGRESS" if start_date == date.today() else "CREATED"
        serializer.save(status=status_value)

def ProjectListView(request):
    from rest_framework.renderers import JSONRenderer
    viewset = ProjectViewSet.as_view({'get': 'list'})
    return viewset(request)


def ProjectDetailView(request, pk):
    viewset = ProjectViewSet.as_view({'get': 'retrieve'})
    return viewset(request, pk=pk)


def ProjectCreateView(request):
    viewset = ProjectViewSet.as_view({'post': 'create'})
    return viewset(request)
