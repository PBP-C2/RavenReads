import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from main.forms import MainThreadForm, PersonForm, ThreadForm
from main.models import Book, MainThread, Person, ReadingProgress, Thread

import csv
from django.shortcuts import render
from .models import Book
# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    person = Person.objects.all()
    context = {
        'user': request.user,
        'person': person,
    }

    return render(request, "main.html", context)

def register(request):
    form_user = UserCreationForm()
    form_person = PersonForm()

    if request.method == "POST":
        form_user = UserCreationForm(request.POST)
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
    main_thread = MainThread.objects.all()
    thread = Thread.objects.all()
    form = MainThreadForm()

    if request.method == "POST":
        form = MainThreadForm(request.POST)
        if form.is_valid():
            main_thread = form.save(commit=False)
            main_thread.user = request.user
            main_thread.thread_count = 0
            main_thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            return redirect('main:forum_discussion')

    context = {
        'user': request.user,
        'main_thread': main_thread,
        'thread': thread,
        'form': form,
    }
    return render(request, 'forum_discussion.html', context)

def make_thread(request):
    form = MainThreadForm()

    if request.method == "POST":
        form = MainThreadForm(request.POST)
        if form.is_valid():
            main_thread = form.save(commit=False)
            main_thread.user = request.user
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
    form = MainThreadForm()

    if request.method == "POST":
        form = MainThreadForm(request.POST)
        if form.is_valid():
            main_thread = form.save(commit=False)
            main_thread.user = request.user
            main_thread.thread_count = 0
            main_thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            return redirect('main:forum_discussion')

    context = {
        'user': request.user,
        'main_thread': main_thread,
        'thread': thread,
        'form': form,
        'main_thread_id':id,
    }
    return render(request, 'open_main_thread.html', context)

def reply(request, id):
    main_thread = MainThread.objects.get(pk=id)
    form = ThreadForm()

    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.user
            thread.main_thread = main_thread
            thread.save()
            messages.success(request, 'Your thread has been successfully created!')
            return redirect('main:forum_discussion')

    context = {
        'user': request.user,
        'main_thread': main_thread,
        'form': form,
    }
    return render(request, 'reply.html', context)


def import_books_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Book.objects.create(
                title=row['title'],
                cover=row['cover'],
                pages=int(row['pages']),
                author=row['author'],
                rating=float(row['rating']),
                price=int(row['price']),
                description=row['description']
            )

def book_store(request):
    # Panggil fungsi import_books_from_csv dengan menyediakan path ke file CSV dataset
    file_path = 'D:\My Documents\College Task 3\PBP\tugas_kelompok\books.csv'  
    import_books_from_csv(file_path)
    # Query untuk mengambil semua objek Book dari basis data
    books = Book.objects.all()

    context = {
        'books': books,  # Kirim daftar buku ke template
    }
    return render(request, 'book_store.html', context)

# @login_required(login_url='/login')
def book_progression(request):
    return render(request, 'book_progression.html')

def get_reading_progress(request):
    progress = ReadingProgress.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', progress))