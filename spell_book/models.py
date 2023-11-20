from django.db import models
from main.models import Person

# Create your models here.

class Scroll(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)


