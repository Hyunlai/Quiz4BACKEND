from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

from .views import ProjectListView, ProjectDetailView
from .views import ProjectCreateView

urlpatterns = [
    path('create/', ProjectCreateView, name='project-create'),
    path('list/', ProjectListView, name='project-list'),
    path('detail/<int:pk>/', ProjectDetailView, name='project-detail'),
]

