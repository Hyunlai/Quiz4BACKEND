from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'task_name', 'task_description', 'status', 'hours_consumed', 'user_assigned', 'start_date', 'end_date']
