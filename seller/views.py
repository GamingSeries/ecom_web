from django.shortcuts import render

# Create your views here.

def acc_view(request):
    return render (request, 'seller/acc_view.html')