from django.urls import path, include

from backend.ClickUp import admin
from .views import getRoutes, getTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routes/', getRoutes, name='routes'),
    path('Task/', getTask, name='Task'),
    path('Projects/', include('ClickUp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/projects/', include('project.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/', include('ClickUp.urls')),
]
