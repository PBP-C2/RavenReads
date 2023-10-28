from django.shortcuts import render
from spell_book.models import Scroll
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def main_page(request):
    scroll = Scroll.objects.all()
    context = {
        "scrolls": scroll
    }
    return render(request, 'main_whole.html', context)

def get_scroll_json_by_id(request, ID):
    scroll = Scroll.objects.get(pk=ID)
    return HttpResponse(serializers.serialize('json', [scroll]))
