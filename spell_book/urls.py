from django.urls import path
from spell_book.views import main_page, get_scroll_json

app_name = 'spell_book'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('get_scroll_json/', get_scroll_json, name='get_scroll_json')
]