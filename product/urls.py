from django.urls import path
from product.views import show_sub_cat, show_sub_cat_det, ShowProduct,Detail_Product

app_name = 'product'

urlpatterns = [
    path('detailproduct/<int:pk>/',Detail_Product.as_view(),name="detail_product"),
    path('sub_cat/', show_sub_cat, name='sub_cat'),
    path('sub_cat_det/<str:cat>', show_sub_cat_det, name='sub_cat_det'),
    path('show_product/<str:sub_cat>', ShowProduct.as_view(), name='show_product'),
]