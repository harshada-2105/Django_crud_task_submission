from django.urls import path
from .views import *

urlpatterns = [
    path("book_list/", book_list, name="book_list"),
    path("book_create/", book_create, name="book_create"),
    path("<int:pk>/book_delete/", book_delete, name="book_delete"),
    path("<int:pk>/book_update/", book_update, name="book_update"),
]