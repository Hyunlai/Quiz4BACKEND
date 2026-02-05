from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView, name='task-list'),
    path('<int:pk>/', views.TaskDetailView, name='task-detail'),
    path('create/', views.TaskCreateView, name='task-create'),
]
