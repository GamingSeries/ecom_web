from django.urls import path
from .views import acc_view

urlpatterns = [
    path('acc_view/', acc_view, name='acc_view')
    path('seller_info/', seller_info, name='seller_info')
]