from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('_list/', views.ProjectListView, name='project-list'),
    path('<int:pk>/', views.ProjectDetailView, name='project-detail'),
    path('create/', views.ProjectCreateView, name='project-create'),
]

