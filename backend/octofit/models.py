from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('run', 'Running'),
        ('walk', 'Walking'),
        ('strength', 'Strength Training'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration_minutes = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User)

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)
