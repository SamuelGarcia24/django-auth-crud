from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    def __str__(self):
        return f'{self.title} - by {self.user.username}'
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)