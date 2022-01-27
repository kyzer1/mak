from os import name
from django.urls import path
from .views import show_cart
from .views import  reduce_quantity_item,order_summary

app_name = 'cart'

urlpatterns = [
    path('show_cart/',show_cart,name="show_cart"),
    path('reduce-quantity-item/<pk>/',
    reduce_quantity_item, name='reduce-quantity-item'),
    path('order-summary',order_summary,name='order-summary'),
]  





