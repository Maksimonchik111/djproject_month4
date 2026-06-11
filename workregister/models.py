from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=25, default='m')
    link_to_resume = models.URLField()
    position = models.CharField(max_length=150)
    experience_years = models.IntegerField()
    views = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.username
