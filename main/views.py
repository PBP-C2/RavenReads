import csv
import datetime
import json

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from main.forms import MainThreadForm, PersonForm, ThreadForm, UserForm
# from main.models import MainThread, Person, ReadingProgress, Thread
from main.models import (Book, BookStore, Checkout, MainThread, Person,
                         ReadingProgress, Thread)

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    person = Person.objects.get(user=request.user)
    context = {
        'user': request.user,
        'person': person,
    }

    return render(request, "main.html", context)

def register(request):
    form_user = UserForm()
    form_person = PersonForm()

    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_person = PersonForm(request.POST)
        if form_user.is_valid() and form_person.is_valid():
            user = form_user.save()  # Save the user object
            person_data = form_person.cleaned_data
            person = Person(
                user=user,
                name=person_data['name'],
                email=person_data['email'],
                tipe=person_data['tipe'],
                gender=person_data['gender']
            )
            person.save()  # Save the Person object
            messages.success(request, 'Your account and profile have been successfully created!')
            return redirect('main:login')
        else:
            messages.error(request, 'Sorry, there was an error creating your account and profile. Please try again.')
    context = {'form':form_user, 'form_person':form_person}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

@login_required(login_url='/login')
def forum_discussion(request):
    wizard = Person.objects.filter(tipe="Wizard")
    muggle = Person.objects.filter(tipe="Muggle")
    main_thread = MainThread.objects.all()
    wizard_thread = MainThread.objects.filter(person__in=wizard)
    muggle_thread = MainThread.objects.filter(person__in=muggle)
    thread = Thread.objects.all()
    form = MainThreadForm()

    if request.method == "POST":
        form = MainThreadForm(request.POST)
        if form.is_valid():
            main_thread = form.save(commit=False)
            main_thread.person = Person.objects.get(user=request.user)
            main_thread.thread_count = 0
            main_thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            return redirect('main:forum_discussion')

    context = {
        'user': request.user,
        'main_thread': main_thread,
        'thread': thread,
        'form': form,
        'wizard_thread': wizard_thread,
        'muggle_thread': muggle_thread,
    }
    return render(request, 'forum_discussion.html', context)

def make_thread(request):
    form = MainThreadForm()

    if request.method == "POST":
        form = MainThreadForm(request.POST)
        if form.is_valid():
            main_thread = form.save(commit=False)
            main_thread.person = Person.objects.get(user=request.user)
            main_thread.thread_count = 0
            main_thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            return redirect('main:forum_discussion')
        
    context = {
        'form': form,
    }
    return render(request, 'make_thread.html', context)

def open_main_thread(request, id):
    main_thread = MainThread.objects.get(pk=id)
    thread = Thread.objects.filter(main_thread=main_thread)
    form = ThreadForm()

    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.person = Person.objects.get(user=request.user)
            thread.main_thread = main_thread
            thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            url = reverse("main:open_main_thread", kwargs={"id":id})
            return redirect(url)

    context = {
        'user': request.user,
        'main_thread': main_thread,
        'thread': thread,
        'form': form,
        'main_thread_id':id,
    }
    return render(request, 'open_main_thread.html', context)

def get_thread_json(request, id):
    main_thread = MainThread.objects.get(pk=id)
    thread = Thread.objects.filter(main_thread=main_thread)
    return HttpResponse(serializers.serialize('json', thread))

def reply(request, id):
    main_thread = MainThread.objects.get(pk=id)
    form = ThreadForm()

    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.person = Person.objects.get(user=request.user)
            thread.main_thread = main_thread
            thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            url = reverse("main:open_main_thread", kwargs={"id":id})
            return redirect(url)

    context = {
        'user': request.user,
        'main_thread': main_thread,
        'form': form,
    }
    return render(request, 'reply.html', context)

def get_main_thread_wizard_json(request):
    wizard = Person.objects.filter(tipe="Wizard")
    wizard_thread = MainThread.objects.filter(person__in=wizard)
    return HttpResponse(serializers.serialize('json', wizard_thread))

def get_main_thread_muggle_json(request):
    muggle = Person.objects.filter(tipe="Muggle")
    muggle_thread = MainThread.objects.filter(person__in=muggle)
    return HttpResponse(serializers.serialize('json', muggle_thread))

@csrf_exempt
def new_main_thread_ajax(request):
    if request.method == 'POST':
        person = Person.objects.get(user=request.user)
        title = request.POST.get("title")
        content = request.POST.get("content")
        thread_count = 0

        new_main_thread = MainThread(title=title, content=content, person=person, thread_count=thread_count)
        new_main_thread.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

import json
import os

from django.conf import settings


def get_books_from_json(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'book', 'fixtures', 'Books.json')
    with open('book/fixtures/Books.json', 'r') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)

def book_store(request):
    context = {}
    try : 
        # Ambil data dari model BookStore
        bookstores = BookStore.objects.all()

        # Gabungkan data dari model BookStore
        combined_data = []
        for bookstore in bookstores:
            data = {
                "title": bookstore.title,
                "cover": bookstore.cover.url,
                "author": bookstore.author,
                "rating": float(bookstore.rating),
                "price": int(bookstore.price),
                "description": bookstore.description
            }
            combined_data.append(data)

        context = {
            'books': combined_data,
        }
    except Exception as error:
        print("Gagal mengambil data buku:", error)

    return render(request, 'book_store.html', context)


def add_checkout_ajax(request):
    if request.method == 'POST':
        book_id = request.POST.get("book_id")
        book = Book.objects.get(pk=book_id)
        user = request.user

        new_checkout = Checkout(user=user, book=book)
        new_checkout.save()

        return HttpResponse("Checkout added", status=201)

    return HttpResponseNotFound()

def see_checkout_ajax(request):
    if request.method == 'GET':
        user = request.user
        checkouts = Checkout.objects.filter(user=user)

        checkout_books = [checkout.book for checkout in checkouts]

        data = serializers.serialize('json', checkout_books)
        return HttpResponse(data)

    return HttpResponseNotFound()


# @login_required(login_url='/login')
def book_progression(request):
    return render(request, 'book_progression.html')

def get_reading_progress(request):
    progress = ReadingProgress.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', progress))

def magic_quiz(request):
    return render(request, 'magic_quiz.html')
