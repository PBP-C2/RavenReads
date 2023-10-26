from django.urls import path
from main.views import show_main, login_user, register, forum_discussion, logout_user, make_thread, open_main_thread, reply, get_main_thread_json, new_main_thread_ajax

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
    path('get_main_thread_json/', get_main_thread_json, name='get_main_thread_json'),
    path('new_main_thread_ajax/', new_main_thread_ajax, name='new_main_thread_ajax')
]