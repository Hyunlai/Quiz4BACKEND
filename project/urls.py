from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

from .views import ProjectListView, ProjectDetailView
from .views import ProjectCreateView

urlpatterns = [
    path('', views.ProjectListView, name='project-list'),
    path('<int:pk>/', views.ProjectDetailView, name='project-detail'),
    path('create/', views.ProjectCreateView, name='project-create'),
]

