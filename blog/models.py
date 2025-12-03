from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

class Book(models.Model):
    isbn = models.CharField(max_length=13, null=False, blank=False, unique=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT)
    authors = models.ManyToManyField(Author)

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'author'], name='unique_book_author'
            )
        ]
