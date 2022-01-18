from django.urls import path
from .views import OrderSummaryView, reduce_quantity_item

app_name = 'cart'


urlpatterns = [
   path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
   path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item')
]