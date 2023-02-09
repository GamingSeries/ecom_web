from django.shortcuts import render, redirect
from .forms import ItemForm

# Create your views here.

def acc_view(request):
    form = ItemForm()
    
    if request.method == 'POST':
        data = request.POST
        form = ItemForm(data)
        if form.is_valid():
            form.save()
            redirect('exfore : home.html')
        else:
            print(form.errors)
    return render (request, 'seller/acc_view.html', {'form' : form})