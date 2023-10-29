from django.shortcuts import render
from spell_book.models import Scroll
from main.models import Person
from spell_book.forms import CreatingScrolls
from django.shortcuts import redirect
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse

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
        
    recent = None
    if 'recently_made' in request.session:
        recent = Scroll.objects.filter(pk__in=request.session['recently_made'])
    else:
        recent = None

    context = {
        "scrolls": Scroll.objects.filter(person=person_login),
        "form": form,
        "recently_made": recent
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

def new_scroll_ajax(request):
    if request.method == "POST":
        person = Person.objects.get(user=request.user)
        title = request.POST.get("title")
        image_url = request.POST.get("image_url")
        content = request.POST.get("content")

        new_scroll = Scroll(title=title, image_url=image_url, content=content, person=person)
        new_scroll.save()

        # Session
        if 'recently_made' in request.session:
            request.session['recently_made'].insert(0, new_scroll.id)
        else:
            request.session['recently_made'] = [new_scroll.id]
        
        request.session.modified = True
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_session_data(request):
    data_from_session = request.session.get('recently_made', [])
    return JsonResponse({'data': data_from_session})