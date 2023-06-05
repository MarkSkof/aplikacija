from django.contrib import admin
from django.urls import path, include
from .views import populate_database


urlpatterens = [
    path('populate_database/', populate_database)
]