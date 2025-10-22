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
    return render(request, 'loops.html', contexto)