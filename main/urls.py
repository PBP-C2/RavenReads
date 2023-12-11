from django.urls import path
from main.views import show_main, login_user, register, forum_discussion, logout_user, make_thread, open_main_thread, reply, get_main_thread_wizard_json, new_main_thread_ajax
from main.views import get_main_thread_muggle_json, get_thread_json, new_thread_ajax, filter_thread_by_user, get_person_name, get_main_thread_by_id

from main.views import (add_checkout_ajax, book_progression, book_store,
                        forum_discussion, get_books_from_json,
                        get_main_thread_muggle_json,
                        get_main_thread_wizard_json, get_reading_progress,
                        get_thread_json, login_user, logout_user, magic_quiz,
                        make_thread, new_main_thread_ajax, new_thread_ajax, open_main_thread,
                        register, reply, see_checkout_ajax, show_main, create_main_discussion_flutter, reply_discussion_flutter, get_person_name_flutter)
from main.views import (book_progression, book_store, forum_discussion,
                        get_reading_progress, post_quiz_points_flutter,
                        login_user, logout_user, make_thread, open_main_thread,
                        register, reply, show_main, increment_progress, add_review, get_reading_progress_by_id, magic_quiz, quiz_points, quiz_results, show_about, add_progression, get_person_type)

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
    path('get-person-type/', get_person_type, name='get_person_type'),
    path('get-progression/', get_reading_progress, name='get_reading_progress'),
    path('get-progression/<int:id>/', get_reading_progress_by_id, name='get_reading_progress_by_id'),
    path('increment-progress/<int:id>/', increment_progress, name='increment_progress'),
    path('add-review/<int:id>/', add_review, name='add_review'),
    path('add-progression/', add_progression, name='add_progression'),
    path('book_store/', book_store, name='book_store'),
    path('magic_quiz/', magic_quiz, name='magic_quiz'),
    path('get_books_from_json/', get_books_from_json, name='get_books_from_json'),
    path('see_checkout_ajax/',see_checkout_ajax,name ='see_checkout_ajax'),
    path('add_checkout_ajax/',add_checkout_ajax,name='add_checkout_ajax'),
    path('get-progression/<int:id>/', get_reading_progress_by_id, name='get_reading_progress_by_id'),
    path('increment-progress/<int:id>/', increment_progress, name='increment_progress'),
    path('add-review/<int:id>/', add_review, name='add_review'),
    path('magic_quiz/', magic_quiz, name='magic_quiz'),
    path('quiz_points/', quiz_points, name='quiz_points'),
    path('quiz_results/', quiz_results, name='quiz_results'),
    path('new_thread_ajax/<int:id>', new_thread_ajax, name='new_thread_ajax'),
    path('filter_thread_by_user/<int:id>', filter_thread_by_user, name='filter_thread_by_user'),
    path('get_person_name/<int:id>', get_person_name, name='get_person_name'),
    path('about/', show_about, name='show_about'),
    path('create_main_discussion_flutter/', create_main_discussion_flutter, name='create_main_discussion_flutter'),
    path('reply_discussion_flutter/', reply_discussion_flutter, name='reply_discussion_flutter'),
    path('post_quiz_points_flutter/', post_quiz_points_flutter, name='post_quiz_points_flutter'),
    path('get_person_name_flutter/<int:id>', get_person_name_flutter, name='get_person_name_flutter'),
    path('get_main_thread_by_id/<int:id>', get_main_thread_by_id, name='get_main_thread_by_id'),
]