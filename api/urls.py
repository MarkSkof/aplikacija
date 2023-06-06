from django.contrib import admin
from django.urls import path, include
from .views import populate_database, post_list, \
                   user_list, comment_list, todo_list, \
                   post_detail, user_detail, comment_detail, \
                   todo_detail, user_posts, post_comments


urlpatterens = [
    path('populate_database/', populate_database),
    path('post/', post_list),
    path('post/<int:id>/', post_detail),
    path('post/<int:id>/comments/', post_comments),
    path('user/', user_list),
    path('user/<int:id>/', user_detail),
    path('user/<int:id>/posts/', user_posts),
    path('comment/', comment_list),
    path('comment/<int:id>/', comment_detail),
    path('todo/', todo_list),
    path('todo/<int:id>/', todo_detail)

]