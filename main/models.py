from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tipe = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)