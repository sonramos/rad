from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, JsonResponse
from datetime import date
from .models import Publisher, Author, Book
from .forms import PublisherForm, AuthorForm, BookForm

def home(request):
    # Simulação de posts de blog
    posts = [
        {
            "titulo": "O Senhor dos Anéis",
            "autor": "J.R.R. Tolkien",
            "data": "1954",
            "descricao": "Uma das maiores obras de fantasia épica da literatura mundial."
        },
        {
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "data": "1899",
            "descricao": "Um clássico brasileiro que discute ciúme, dúvida e memória."
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "data": "1949",
            "descricao": "Uma crítica poderosa ao totalitarismo e vigilância estatal."
        }
    ]

    contexto = {
        "usuario": "sonramos",
        "data_atual": date.today(),
        "posts": posts
    }
    return render(request, "blog/home.html", contexto)


def contato(request, contact_number):
    contatos = [
        {'nome': 'Jackson', 'numero': 83999999999},
        {'nome': 'Edemberg', 'numero': 83988888888},
        {'nome': 'Cândido', 'numero': 83977777777},
    ]

    contato_selecionado = contatos[contact_number - 1]

    contexto = {
        'contato': contato_selecionado,
        'contact_number': contact_number,
        'contatos': contatos
    }
    return render(request, "blog/contato.html", contexto)


def about(request):
    contexto = {
        "usuario": "Jackson Ramos"
    }
    return render(request, "blog/about.html", contexto)

# -------------------- PUBLISHER --------------------

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, "blog/publisher/list.html", {"publishers": publishers})

def publisher_detail(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    return render(request, "blog/publisher/detail.html", {"publisher": publisher})

def publisher_create(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("publisher_list")
    return render(request, "blog/publisher/form.html", {"form": form})

def publisher_update(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    form = PublisherForm(request.POST or None, instance=publisher)
    if form.is_valid():
        form.save()
        return redirect("publisher_list")
    return render(request, "blog/publisher/form.html", {"form": form})

def publisher_delete(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    if request.method == "POST":
        publisher.delete()
        return redirect("publisher_list")
    return render(request, "blog/publisher/delete.html", {"publisher": publisher})

# -------------------- AUTHOR --------------------

def author_list(request):
    authors = Author.objects.all()
    return render(request, "blog/author/list.html", {"authors": authors})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author/detail.html", {"author": author})

def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("author_list")
    return render(request, "blog/author/form.html", {"form": form})

def author_update(request, id):
    author = get_object_or_404(Author, id=id)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect("author_list")
    return render(request, "blog/author/form.html", {"form": form})

def author_delete(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == "POST":
        author.delete()
        return redirect("author_list")
    return render(request, "blog/author/delete.html", {"author": author})

# -------------------- BOOK --------------------

def book_list(request):
    books = Book.objects.all()
    return render(request, "blog/book/list.html", {"books": books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "blog/book/detail.html", {"book": book})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "blog/book/form.html", {"form": form})

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "blog/book/form.html", {"form": form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "blog/book/delete.html", {"book": book})
