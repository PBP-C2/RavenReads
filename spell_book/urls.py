from django.urls import path
from spell_book.views import main_page, get_scroll_json, new_scroll_ajax, get_session_data, create_product_flutter, show_scroll_data_json, get_product_json

app_name = 'spell_book'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('get_scroll_json/', get_scroll_json, name='get_scroll_json'),
    path('new_scroll_ajax/', new_scroll_ajax, name='new_scroll_ajax'),
    path('get_session_data', get_session_data, name='get_session_data'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('show_scroll_data/', show_scroll_data_json, name='show_scroll_data_json'),
    path('show_scroll/', get_product_json, name='show_scroll'),
]