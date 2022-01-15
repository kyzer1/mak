from django.urls import path
from .views import show_sub_cat, show_sub_cat_det, ShowProductBySubCategory, ShowProductCategory, ProductList

app_name = 'product'

urlpatterns = [

    path('sub_cat/', show_sub_cat, name='sub_cat'),
    path('sub_cat_det/<str:cat>', show_sub_cat_det, name='sub_cat_det'),
    path('show_product_sub_cat/<str:sub_cat>', ShowProductBySubCategory.as_view(), name='show_product_sub_cat'),
    path('show_product_cat/<int:id>', ShowProductCategory.as_view(), name='show_product_cat'),
    path('show_product/', ProductList.as_view(), name='show_product'),
]