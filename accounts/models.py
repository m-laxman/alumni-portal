from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AbstractUser
# Create your models here.

class RegisteredUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    usertype = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.first_name
