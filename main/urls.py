from django.urls import path
from main.views import book_store, get_reading_progress, show_main, login_user, register, forum_discussion, logout_user, make_thread, open_main_thread, reply, get_main_thread_wizard_json, new_main_thread_ajax
from main.views import get_main_thread_muggle_json, get_thread_json

from main.views import (book_progression, forum_discussion,
                        get_reading_progress,
                        login_user, logout_user, make_thread, open_main_thread,
                        register, reply, show_main, magic_quiz)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('discussion/', forum_discussion, name='forum_discussion'),
    path('logout/', logout_user, name='logout'),
    path('make_thread/', make_thread, name='make_thread'),
    path('discussion/<int:id>/', open_main_thread, name='open_main_thread'),
    path('discussion/<int:id>/reply/', reply, name='reply'),
    path('get_wizard_json/', get_main_thread_wizard_json, name='get_wizard_json'),
    path('get_muggle_json/', get_main_thread_muggle_json, name='get_muggle_json'),
    path('new_main_thread_ajax/', new_main_thread_ajax, name='new_main_thread_ajax'),
    path('get_thread_json/<int:id>', get_thread_json, name='get_thread_json'),
    path('book-progression/', book_progression, name='book_progression'),
    path('get-progression/', get_reading_progress, name='get_reading_progress'),
    path('book_store/', book_store, name='book_store'),
    path('magic_quiz/', magic_quiz, name='magic_quiz')
]