"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

def getRoutes(request):
    routes = [
        {'GET': '/api/routes/', 'description': 'List all available routes'},
        {'GET': '/api/projects/', 'description': 'List all projects'},
        {'GET': '/api/projects/<id>/', 'description': 'Get project details'},
        {'POST': '/api/projects/', 'description': 'Create a new project'},
        {'GET': '/api/tasks/', 'description': 'List all tasks'},
        {'GET': '/api/tasks/<id>/', 'description': 'Get task details'},
        {'POST': '/api/tasks/', 'description': 'Create a new task'},
        {'GET': '/api/users/', 'description': 'List all users'},
        {'GET': '/api/users/<id>/', 'description': 'Get user details'},
        {'POST': '/api/users/', 'description': 'Create a new user'},
    ]
    return JsonResponse(routes, safe=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/routes/', getRoutes, name='routes'),
    path('api/projects/', include('project.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
