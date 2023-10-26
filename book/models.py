from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(null=True, blank=True, max_length=256)
    title = models.CharField(null=True, blank=True, max_length=256)
    author = models.CharField(null=True, blank=True, max_length=256)
    year_publication = models.IntegerField(null=True, blank=True, max_length=256)
    publisher = models.CharField(null=True, blank=True, max_length=256)
    image_url_s = models.CharField(null=True, blank=True, max_length=256)
    image_url_m = models.CharField(null=True, blank=True, max_length=256)
    image_url_l = models.CharField(null=True, blank=True, max_length=256)
