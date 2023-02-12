from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/home.html', stuff_for_frontend)

def cart(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/cart.html', stuff_for_frontend)

def login(request):
    stuff_for_frontend = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'exfire/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'exfire/login.html', stuff_for_frontend)

def register(request):
    stuff_for_frontend = {}

    return render(request, 'exfire/register.html', stuff_for_frontend)