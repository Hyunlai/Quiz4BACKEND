from django.shortcuts import render
from django.http import JsonResponse
from functools import wraps
from django.views.decorators.http import require_http_methods

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

def getRoutes(request):
    routes = [
        {'GET': '/api/users/'},
        {'GET': '/api/users/<id>/', 'description': 'Get user details'},
        {'POST': '/api/users/create/', 'description': 'Create a new user'},
    ]
    return JsonResponse(routes, safe=False)

@require_http_methods(["GET"])
@admin_or_manager_required
def UserListView(request):
    from .models import CustomUserModel

    users = CustomUserModel.objects.all()
    users_data = [
        {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'role': user.role,
        }
        for user in users
    ]
    return JsonResponse(users_data, safe=False)

@require_http_methods(["GET"])
@authenticated_required
def UserDetailView(request, pk):
    from .models import CustomUserModel

    try:
        user = CustomUserModel.objects.get(pk=pk)
    except CustomUserModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    user_data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'role': user.role,
    }
    return JsonResponse(user_data)

@require_http_methods(["POST"])
@admin_required
def UserCreateView(request):
    from .models import CustomUserModel
    import json

    try:
        data = json.loads(request.body)
        new_user = CustomUserModel.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['username'],
            email=data['email'],
            role=data['role']
        )
        new_user.save()
        return JsonResponse({'message': 'User created successfully', 'user_id': new_user.id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
@require_http_methods(["GET"])
@authenticated_required
def CurrentUserView(request):
    from .models import CustomUserModel

    username = get_username(request)
    try:
        user = CustomUserModel.objects.get(username=username)
    except CustomUserModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    user_data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'role': user.role,
    }
    return JsonResponse(user_data)

@require_http_methods(["POST"])
@admin_required
def UserDeleteView(request, pk):
    from .models import CustomUserModel

    try:
        user = CustomUserModel.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=200)
    except CustomUserModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)