from django.urls import path
from django import views

urlpatterns = [
    path("hello", views.say_hello)
]



