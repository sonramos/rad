from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(request):
    return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, text):
    return HttpResponse(f"Você digitou: {text}")

def api_info(request):
    info = {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  }
    return JsonResponse(info)