from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView, name='project-list'),
    path('<int:pk>/', views.ProjectDetailView, name='project-detail'),
    path('create/', views.ProjectCreateView, name='project-create'),
]

