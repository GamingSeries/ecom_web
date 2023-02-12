from seller.models import Merchant
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import ItemForm

# Create your views here.

def acc_view(request):
    form = ItemForm()
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        print(form.errors)
    
    return render(request, 'seller/acc_view.html', {'form': form})

def seller_info(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = make_password(password)

        seller = Merchant(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            password=hashed_password,
            address=request.POST.get('address')
        )
        seller.save()
        
    return render(request, 'seller/seller_info.html')