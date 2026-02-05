from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView, name='user-list'),
    path('<int:pk>/', views.UserDetailView, name='user-detail'),
    path('create/', views.UserCreateView, name='user-create'),
]
