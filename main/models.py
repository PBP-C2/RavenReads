from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tipe = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

class MainThread(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.ImageField(upload_to='images/')
    thread_count = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Thread(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    main_thread = models.ForeignKey(MainThread, on_delete=models.CASCADE)
    content = models.TextField()
    images = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)