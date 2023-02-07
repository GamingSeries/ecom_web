from django.shortcuts import render
# Create your views here.

def home(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/home.html', stuff_for_frontend)

def cart(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/cart.html', stuff_for_frontend)

def login(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/login.html', stuff_for_frontend)

def register(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/register.html', stuff_for_frontend)