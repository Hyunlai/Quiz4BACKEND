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