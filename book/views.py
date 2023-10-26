from django.shortcuts import render
from book.models import Book
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
