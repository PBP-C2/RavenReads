from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
import datetime
from main.models import Person, MainThread, Thread
from main.forms import PersonForm, MainThreadForm, ThreadForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

from main.forms import MainThreadForm, PersonForm, ThreadForm
from main.models import Book, MainThread, Person, ReadingProgress, Thread, QuizPoint

from book.models import Book as Bk

import csv
from django.shortcuts import render
from .models import Book
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
    recently_viewed_thread = None
    
    if 'recently_viewed_thread' in request.session:
        recently_viewed_thread = MainThread.objects.filter(pk__in=request.session['recently_viewed_thread'])
    else:
        recently_viewed_thread = None
        

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
        'users': Person.objects.all(),
        'main_thread': main_thread,
        'thread': thread,
        'form': form,
        'wizard_thread': wizard_thread,
        'muggle_thread': muggle_thread,
        'recent': recently_viewed_thread,
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

    # Untuk session
    if 'recently_viewed_thread' in request.session:
        if id in request.session['recently_viewed_thread']:
            request.session['recently_viewed_thread'].remove(id)
        
        request.session['recently_viewed_thread'].insert(0, id)
        if len(request.session['recently_viewed_thread']) > 5:
            request.session['recently_viewed_thread'].pop()
    else:
        request.session['recently_viewed_thread'] = [id]

    request.session.modified = True

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

def new_thread_ajax(request, id):
    if request.method == 'POST':
        person = Person.objects.get(user=request.user)
        main_thread = MainThread.objects.get(pk=id)
        content = request.POST.get("content")

        new_thread = Thread(content=content, person=person, main_thread=main_thread)
        new_thread.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def filter_thread_by_user(request, id):
    thread = MainThread.objects.filter(person=Person.objects.get(pk=id))
    return HttpResponse(serializers.serialize('json', thread))

def get_person_name(request, id):
    person = Person.objects.get(pk=id)
    return HttpResponse(serializers.serialize('json', [person]))

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

    # context = {
    #     'books': books,  # Kirim daftar buku ke template
    # }
    return render(request, 'book_store.html')

@login_required(login_url='/login')
def book_progression(request):
    person = Person.objects.get(user=request.user)
    if person.tipe == "Wizard":
        return render(request, 'book_progression.html')
    return HttpResponseRedirect(reverse('main:show_main'))

def get_reading_progress(request):
    progresses = ReadingProgress.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', progresses))

def get_reading_progress_by_id(request, id):
    progresses = ReadingProgress.objects.filter(user=request.user)
    progress = progresses.get(pk=id)
    return HttpResponse(serializers.serialize('json', progress))

def increment_progress(request, id):
    if request.method == 'POST':
        progress = ReadingProgress.objects.filter(user=request.user)
        current_progress = progress.get(pk=id)
        if current_progress.book.pages > current_progress.progress:
            current_progress.progress += 1
            current_progress.save()
        return HttpResponse(b"OK", status=200)
    
    return HttpResponseNotFound()

@csrf_exempt
def add_review(request, id):
    if request.method == 'POST':
        progress = ReadingProgress.objects.filter(user=request.user)
        current_progress = progress.get(pk=id)
        current_progress.rating = request.POST.get("rating")
        current_progress.review = request.POST.get("review")
        current_progress.save()
        return HttpResponse(b"OK", status=200)
    
    return HttpResponseNotFound()

@csrf_exempt
def add_progression(request):
    if request.method == 'POST':
        user = request.user
        bookId = request.POST.get("newBook")
        book = Bk.objects.get(pk = bookId)
        existing_progress = ReadingProgress.objects.filter(user=user, book=book).first()
        if existing_progress:
            return HttpResponse(b"Duplicate entry - This book is already in progress for this user", status=400)
        else:
            new_progress = ReadingProgress(user=user, book=book)
            new_progress.save()
            return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url='/login')
def magic_quiz(request):
    user = request.user
    points = 0
    if user.is_authenticated:
        user_points = QuizPoint.objects.filter(user=user)
        if user_points.exists():
            user_data = user_points.first()
            points = user_data.points
    context = {
        'points': points
    }
    return render(request, 'magic_quiz.html', context)

def quiz_points(request):
    if request.method == 'POST':
        total_points = request.POST.get('total_points', 0)
        user = request.user
        if user.is_authenticated:
            quiz_point, created = QuizPoint.objects.get_or_create(user=user)
            quiz_point.points = total_points
            quiz_point.save()
        return HttpResponseRedirect(reverse('main:quiz_results'))
    
def quiz_results(request):
    data = Book.objects.all()
    user = get_object_or_404(QuizPoint, user=request.user)
    books = {
        'booklist': data,
        'userPoints': user.points
    }
    return render(request, "quiz_results.html", books)
    
def show_about(request):
    return render(request, "about.html")
