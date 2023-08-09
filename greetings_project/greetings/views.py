from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to the Greetings App!")

def greet_user(request, username):
    return HttpResponse(f"Hello, {username}!")

def farewell_user(request, username):
    return HttpResponse(f"Goodbye, {username}!")
