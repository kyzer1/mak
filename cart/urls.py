from django.urls import path
from .views import show_cart
from .views import OrderSummaryView, reduce_quantity_item

app_name = 'cart'

urlpatterns = [
    path('show_cart/',show_cart,name="show_cart"),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item')
]  





