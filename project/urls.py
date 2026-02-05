from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

from .views import ProjectListView, ProjectDetailView
from .views import ProjectCreateView

urlpatterns = [
    path('api/projects/', ProjectListView, name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailView, name='project-detail'),
    path('api/projects/create/', ProjectCreateView, name='project-create'),
]

