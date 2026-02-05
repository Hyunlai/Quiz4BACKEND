from rest_framework import serializers
from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role']
