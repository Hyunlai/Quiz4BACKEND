from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import TaskCreateView
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('create/', TaskCreateView, name='task-create'),
    path('list/', TaskListView, name='task-list'),
    path('detail/<int:pk>/', TaskDetailView, name='task-detail'),
]
