from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('_list/', views.TaskListView, name='task-list'),
    path('<int:pk>/', views.TaskDetailView, name='task-detail'),
    path('create/', views.TaskCreateView, name='task-create'),
]
