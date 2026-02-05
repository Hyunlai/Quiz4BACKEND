from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('_list/', views.UserListView, name='user-list'),
    path('current/', views.CurrentUserView, name='current-user'),
    path('routes/', views.getRoutes, name='routes'),
]
