from django.urls import path
from main.views import show_main, login_user, register, forum_discussion, logout_user, make_thread, open_main_thread, reply, get_main_thread_wizard_json, new_main_thread_ajax
from main.views import get_main_thread_muggle_json, get_thread_json

from main.views import (book_progression, book_store, forum_discussion,
                        get_reading_progress, import_books_from_csv,
                        login_user, logout_user, make_thread, open_main_thread,
                        register, reply, show_main, increment_progress, add_review, get_reading_progress_by_id, magic_quiz, quiz_points, quiz_results)

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
     path('get-progression/<int:id>/', get_reading_progress_by_id, name='get_reading_progress_by_id'),
    path('increment-progress/<int:id>/', increment_progress, name='increment_progress'),
    path('add-review/<int:id>/', add_review, name='add_review'),
    path('import_books_from_csv/',import_books_from_csv, name='import_books_from_csv'),
    path('magic_quiz/', magic_quiz, name='magic_quiz'),
    path('quiz_points/', quiz_points, name='quiz_points'),
    path('quiz_results/', quiz_results, name='quiz_results')
]