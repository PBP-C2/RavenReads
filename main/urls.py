from django.urls import path

from main.views import (book_progression, book_store, forum_discussion,
                        get_reading_progress, import_books_from_csv,
                        login_user, logout_user, make_thread, open_main_thread,
                        register, reply, show_main, increment_progress, add_review, get_reading_progress_by_id)

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
    path('book-progression/', book_progression, name='book_progression'),
    path('get-progression/', get_reading_progress, name='get_reading_progress'),
    path('get-progression/<int:id>/', get_reading_progress_by_id, name='get_reading_progress_by_id'),
    path('increment-progress/<int:id>/', increment_progress, name='increment_progress'),
    path('add-review/<int:id>/', add_review, name='add_review'),
    path('book_store/', book_store, name='book_store'),
    path('import_books_from_csv/',import_books_from_csv, name='import_books_from_csv')
]