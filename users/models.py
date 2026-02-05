from django.db import models

class CustomUserModel(models.Model):
    ROLES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('User', 'User'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLES)
    
    def __str__(self):
        return self.username
