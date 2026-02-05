from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import TaskCreateView
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('api/tasks/', TaskListView, name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailView, name='task-detail'),
    path('api/tasks/create/', TaskCreateView, name='task-create'),
]
