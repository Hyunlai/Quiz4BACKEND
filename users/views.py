from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from functools import wraps
from .models import CustomUserModel
from .serializers import CustomUserSerializer
from django.http import JsonResponse


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_role = request.session.get('user_role') or getattr(request.user, 'role', None)
        if user_role == 'Admin':
            return view_func(request, *args, **kwargs)
        return JsonResponse({'error': 'Admin access required'}, status=403)
    return wrapper


def admin_or_manager_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_role = request.session.get('user_role') or getattr(request.user, 'role', None)
        if user_role in ['Admin', 'Manager']:
            return view_func(request, *args, **kwargs)
        return JsonResponse({'error': 'Admin or Manager access required'}, status=403)
    return wrapper


def authenticated_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_role = request.session.get('user_role') or getattr(request.user, 'role', None)
        if user_role in ['Admin', 'Manager', 'User']:
            return view_func(request, *args, **kwargs)
        return JsonResponse({'error': 'Authentication required'}, status=403)
    return wrapper


def get_user_role(request):
    return request.session.get('user_role') or getattr(request.user, 'role', None)


def get_username(request):
    return request.session.get('username') or getattr(request.user, 'username', None)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['get'])
    def current_user(self, request):
        username = get_username(request)
        try:
            user = CustomUserModel.objects.get(username=username)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except CustomUserModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


def UserListView(request):
    viewset = CustomUserViewSet.as_view({'get': 'list'})
    return viewset(request)


def UserDetailView(request, pk):
    viewset = CustomUserViewSet.as_view({'get': 'retrieve'})
    return viewset(request, pk=pk)


def UserCreateView(request):
    viewset = CustomUserViewSet.as_view({'post': 'create'})
    return viewset(request)


def CurrentUserView(request):
    viewset = CustomUserViewSet.as_view({'get': 'current_user'})
    return viewset(request)


def UserDeleteView(request, pk):
    viewset = CustomUserViewSet.as_view({'delete': 'destroy'})
    return viewset(request, pk=pk)


def getRoutes(request):
    routes = [
        {'GET': '/api/users/', 'description': 'List all users'},
        {'GET': '/api/users/<id>/', 'description': 'Get user details'},
        {'POST': '/api/users/', 'description': 'Create a new user'},
        {'DELETE': '/api/users/<id>/', 'description': 'Delete a user'},
        {'GET': '/api/users/current/', 'description': 'Get current user'},
    ]
    return JsonResponse(routes, safe=False)