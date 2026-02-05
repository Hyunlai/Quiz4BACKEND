from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import date
from .models import Task
from .serializers import TaskSerializer
from project.models import Project


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def perform_create(self, serializer):
        """Auto-set status based on start_date"""
        start_date = serializer.validated_data.get('start_date')
        status_value = "IN PROGRESS" if start_date == date.today() else "CREATED"
        serializer.save(status=status_value)

def TaskListView(request):
    viewset = TaskViewSet.as_view({'get': 'list'})
    return viewset(request)


def TaskDetailView(request, pk):
    viewset = TaskViewSet.as_view({'get': 'retrieve'})
    return viewset(request, pk=pk)


def TaskCreateView(request):
    viewset = TaskViewSet.as_view({'post': 'create'})
    return viewset(request)
