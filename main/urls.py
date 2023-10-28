from django.urls import path

from main.views import (add_checkout_ajax, book_progression, book_store,
                        forum_discussion, get_books_from_json,
                        get_main_thread_muggle_json,
                        get_main_thread_wizard_json, get_reading_progress,
                        get_thread_json, login_user, logout_user, magic_quiz,
                        make_thread, new_main_thread_ajax, open_main_thread,
                        register, reply, see_checkout_ajax, show_main)

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
    path('magic_quiz/', magic_quiz, name='magic_quiz'),
    path('get_books_from_json/', get_books_from_json, name='get_books_from_json'),
    path('see_checkout_ajax/',see_checkout_ajax,name ='see_checkout_ajax'),
    path('add_checkout_ajax/',add_checkout_ajax,name='add_checkout_ajax'),
]