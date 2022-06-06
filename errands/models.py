from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
