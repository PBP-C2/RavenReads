from django.urls import path, include
from book.views import get_books

app_name = 'book'

urlpatterns = [
    path('', get_books, name='get_books'),
    path('', include('main.urls'))
]