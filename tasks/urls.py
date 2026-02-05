from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.TaskCreateView, name='task-create'),
]
