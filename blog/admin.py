from django.contrib import admin
from .models import Publisher, Author, Book, BookAuthor
# Register your models here.

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'title', 'release_date', 'price', 'stock', 'publisher')
    search_fields = ('title', 'isbn')
    list_filter = ('publisher', 'release_date')

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'author')
    search_fields = ('book__title', 'author__name')