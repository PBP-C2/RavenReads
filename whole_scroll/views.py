from django.shortcuts import render
from spell_book.models import Scroll
from django.http import HttpResponse
from django.core import serializers
from main.models import Person

# Create your views here.

def main_page(request):
    scroll = Scroll.objects.all()
    context = {
        "scrolls": scroll,
        "users": Person.objects.all()
    }
    return render(request, 'main_whole.html', context)

def main_page_by_id(request, ID):
    scroll = Scroll.objects.filter(person=Person.objects.get(pk=ID))
    context = {
        "scrolls": scroll,
        "users": Person.objects.all()
    }
    return render(request, 'main_whole.html', context)
