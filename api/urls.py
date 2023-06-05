from django.contrib import admin
from django.urls import path, include
from .views import populate_database, post_list, user_list, comment_list, todo_list


urlpatterens = [
    path('populate_database/', populate_database),
    path('post/', post_list),
    path('user/', user_list),
    path('comment/', comment_list),
    path('todo/', todo_list)
]