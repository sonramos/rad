from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date

def hello(request):
    contexto = {
        "usuario": "sonramos",
        "frutas": ["pera", "laranja", "uva"],
        "data_atual": date.today(),
        "numero": 37,
    }
    return render(request, "blog/hello.html", contexto)

def eco(request, text):
    return HttpResponse(f"Você digitou: {text}")

def api_info(request):
    info = {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  }
    return JsonResponse(info)

def conditions(request):
    contexto = {
        "is_logged_in": True,
        "age": 31,
        "role": "admin",
    }
    return render(request, "blog/conditions.html", contexto)

def loops(request):
    contexto = {'produtos': [
        {'nome': 'Notebook', 'preco': 3500},
        {'nome': 'Mouse', 'preco': 80},
        {'nome': 'Teclado', 'preco': 150},
    ]}
    return render(request, "blog/loops.html", contexto)

def home(request):
    contexto = {
        "usuario": "sonramos",
        "data_atual": date.today(),
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
        'contact_number': contact_number
    }
    return render(request, "blog/contato.html", contexto)
