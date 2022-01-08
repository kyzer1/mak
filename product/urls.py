from django.urls import path
from .views import products

app_name = 'product'

urlpatterns = [
    path('product/', products, name='products')
    
]