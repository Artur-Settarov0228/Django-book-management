from django.urls import path

from .views import home_view, books_view, add_books_view, delete_books_view, update_books_view

app_name = "books"

urlpatterns = [
    path("", home_view, name="home"),
    path("books/", books_view, name="books"),
    path("books/add/", add_books_view, name="add_books"),
    path("books/delete/", delete_books_view, name="delete_books"),
    path("books/update/", update_books_view, name="update_books"),

]