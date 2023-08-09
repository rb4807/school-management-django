from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    std = models.IntegerField()

    
    def __str__(self):
        return self.name


