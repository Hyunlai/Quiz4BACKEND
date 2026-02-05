from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    status = models.CharField(max_length=50)
    hours_consumed = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    status = models.CharField(max_length=50)
    hours_consumed = models.FloatField()
    user_assigned = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.task_name
    
class CustomUserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username