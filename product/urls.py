from django.urls import path
# from .views import show_sub_cat, show_sub_cat_det, ShowProductBySubCategory, ShowProductCategory, ProductList, FilteringAll
from product.views import show_sub_cat, show_sub_cat_det,Detail_Product
from .views import show_sub_cat, show_sub_cat_det, ProductList, FilteringAll
from product.views import show_sub_cat, show_sub_cat_det ,Detail_Product
from .views import show_sub_cat, show_sub_cat_det, ProductList, FilteringAll
from product.views import show_sub_cat, show_sub_cat_det,Detail_Product,add_to_cart

app_name = 'product'

urlpatterns = [
    path('detailproduct/<int:pk>/',Detail_Product.as_view(),name="detail_product"),
    path('add_to_cart/<int:product_id>',add_to_cart,name='add_to_cart'),
    path('sub_cat/', show_sub_cat, name='sub_cat'),
    path('sub_cat_det/<str:cat>', show_sub_cat_det, name='sub_cat_det'),
    # path('show_product_sub_cat/<str:sub_cat>', ShowProductBySubCategory.as_view(), name='show_product_sub_cat'),
    # path('show_product_cat/<int:id>', ShowProductCategory.as_view(), name='show_product_cat'),
    path('show_product/<str:category>', ProductList.as_view(), name='show_product'),
    path('side_bar_filtering', FilteringAll.as_view(), name='side_bar_filtering'),
]