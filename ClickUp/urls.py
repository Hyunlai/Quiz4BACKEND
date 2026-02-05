from django.urls import path, include
from .views import getRoutes, getTasks
urlpatterns = [
    path('', getRoutes, name='routes'),
    path('tasks/', getTasks, name='tasks'),
]