from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/<int:contact_number>/", views.contato, name="contato"),
    path("about/", views.about, name="about"),

     # Publisher
    path("publishers/", views.publisher_list, name="publisher_list"),
    path("publishers/new/", views.publisher_create, name="publisher_create"),
    path("publishers/<int:id>/", views.publisher_detail, name="publisher_detail"),
    path("publishers/<int:id>/edit/", views.publisher_update, name="publisher_update"),
    path("publishers/<int:id>/delete/", views.publisher_delete, name="publisher_delete"),

    # Author
    path("authors/", views.author_list, name="author_list"),
    path("authors/new/", views.author_create, name="author_create"),
    path("authors/<int:id>/", views.author_detail, name="author_detail"),
    path("authors/<int:id>/edit/", views.author_update, name="author_update"),
    path("authors/<int:id>/delete/", views.author_delete, name="author_delete"),

    # Book
    path("books/", views.book_list, name="book_list"),
    path("books/new/", views.book_create, name="book_create"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),
    path("books/<int:id>/edit/", views.book_update, name="book_update"),
    path("books/<int:id>/delete/", views.book_delete, name="book_delete"),
    
]