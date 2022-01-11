from django.urls import path
from .views import show_sub_cat, show_sub_cat_det, show_product

app_name = 'product'

urlpatterns = [

    path('sub_cat/', show_sub_cat, name='sub_cat'),
    path('sub_cat_det/<str:cat>', show_sub_cat_det, name='sub_cat_det'),
    path('show_product/<str:sub_cat>', show_product, name='show_product'),
]