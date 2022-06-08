from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
