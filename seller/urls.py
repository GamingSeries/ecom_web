from django.urls import path
from .views import add_item, seller_info

urlpatterns = [
    path('add_item/', add_item, name='add_item'),
    path('seller_info/', seller_info, name='seller_info')
]