from django.shortcuts import render
from spell_book.models import Scroll
from main.models import Person
from spell_book.forms import CreatingScrolls
from django.shortcuts import redirect
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def main_page(request):
    person_login = Person.objects.get(user=request.user)
    form = CreatingScrolls()
    if request.method == "POST":
        form = CreatingScrolls(request.POST)
        if form.is_valid():
            scroll = form.save(commit=False)
            scroll.person = Person.objects.get(user=request.user)
            scroll.save()
            return redirect('spell_book:main_page')
        
    context = {
        "scrolls": Scroll.objects.filter(person=person_login),
        "form": form
    }
    return render(request, 'main_page.html', context)

def whole_scroll(request):
    scrolls = Scroll.objects.all()
    context = {
        "scrolls": scrolls
    }
    return render(request, 'whole_scroll.html', context)

def get_scroll_json(request):
    scrolls = Scroll.objects.all()
    return HttpResponse(serializers.serialize('json', scrolls))
