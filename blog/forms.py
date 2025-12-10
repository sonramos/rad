from django import forms
from .models import Book, Author, Publisher, BookAuthor

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'authors': forms.CheckboxSelectMultiple()
        }

class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = BookAuthor
        fields = ['book', 'author']