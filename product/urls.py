from django.urls import path
from .views import products,Detail_Product

app_name = 'product'

urlpatterns = [
    path('detailproduct/<int:pk>/',Detail_Product.as_view(),name="detail_product")
    
]

