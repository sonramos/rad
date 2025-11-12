from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("eco/<str:text>/", views.eco),
    path("info/", views.api_info),
    path("conditions/", views.conditions),
    path("loops/", views.loops),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contato/<int:contact_number>/", views.contato, name="contato"),
]