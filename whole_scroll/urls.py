from django.urls import path
from whole_scroll.views import main_page, get_scroll_json_by_id


app_name = 'whole_scroll'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('get_scroll_json_by_id/<int:ID>', get_scroll_json_by_id, name='get_scroll_json_by_id')
]