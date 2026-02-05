from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView, name='project-list'),
    path('<int:pk>/', views.ProjectDetailView, name='project-detail'),
    path('create/', views.ProjectCreateView, name='project-create'),
    path('<int:pk>/update/', views.ProjectUpdateView, name='project-update'),
    path('<int:pk>/delete/', views.ProjectDeleteView, name='project-delete'),
]
