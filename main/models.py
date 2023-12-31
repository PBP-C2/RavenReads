from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from book.models import Book

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

class BookStore(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.IntegerField()
    description = models.TextField()

    book_reference = models.ForeignKey(Book, on_delete=models.CASCADE)

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default="")
    image = models.CharField(max_length=256, default="")
    pages = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    review = models.TextField(default="")

class QuizPoint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)