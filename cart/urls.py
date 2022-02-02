from os import name
from django.urls import path
from .views import show_cart
from .views import order_summary, faktor

app_name = 'cart'

urlpatterns = [
    path('show_cart/',show_cart,name="show_cart"),
    path('order-summary',order_summary,name='order-summary'),
    path('faktor',faktor,name='faktor')
]  





