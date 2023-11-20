from django.urls import path
from whole_scroll.views import main_page, main_page_by_id


app_name = 'whole_scroll'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('main_page_by_id/<int:ID>', main_page_by_id, name='main_page_by_id')
]