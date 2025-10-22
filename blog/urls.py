from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("eco/<str:text>", views.eco),
    path("info", views.api_info),
    path("conditions", views.conditions),
    path("loops", views.loops),
]