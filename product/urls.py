from django.urls import path

from .views import show_category, products_list,product_details,CategoryView

app_name = 'product'

urlpatterns = [
    # path('product/', ProductList.as_view, name='products'),
    # path('category/', CategoryList.as_view, name='categories')
    path('pro/', show_category, name='productha' ),
    path('shop-list/', products_list, name='shop-list'),
    path('pro-det/', product_details, name="prdetails"),
    path('cat-sho/', CategoryView.as_view(), name="shocat")
    
    

]