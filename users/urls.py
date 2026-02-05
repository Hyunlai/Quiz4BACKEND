from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('api/users/', UserListView, name='user-list'),
    path('api/users/<int:pk>/', UserDetailView, name='user-detail'),
    path('api/users/create/', UserCreateView, name='user-create'),

]
