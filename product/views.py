import sys
from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import CategoryProduct, Product
from supply.models import SalesmanProduct



# print(sys.getrecursionlimit())


# class ProductList (ListView):
#     model = Product
#     context_object_name = "ctx-product"
#     template_name = "header.html"
#     paginate_by = 5


#     def get_queryset(self):
#         qs =super().get_queryset()
#         return qs


# class CategoryList(ListView):
#     model = CategoryProduct
#     context_object_name = "ctx-category"
#     template_name = "header.html"
    

#     def get_queryset(self):
#         qs =super().get_queryset()
#         return qs


def show_category (request):
    top_cat = CategoryProduct.objects.filter(parent__isnull=True)
    top_cat_2 = CategoryProduct.objects.filter(parent__isnull=False)
    
    cnt = {"category" : top_cat, "category2": top_cat_2}
  
    
    return render(request, "header.html", cnt)



def category_view(request, pk):
    catt = get_object_or_404(CategoryProduct, pk = pk)
    gro = CategoryProduct.objects.all()
    cntx = {}
    for g in gro:
        if g.parent_id == pk:
            print(g)

        
    print(catt, pk)
    print(gro)
    return render(request, 'product/base_products.html', {"catt" : catt})



def products_list(request):
    pro=Product.objects.all()
    data=request.GET.get('cat',None)
    selpro = SalesmanProduct.objects.all()

    if data:
        qst = pro.filter(cat__title=data)
        
    return render(request , 'product/shop_list.html', {"qst" : qst, "selpro": selpro})



def product_details (request):
    pro = Product.objects.all()
    sub = request.GET.get('title', '')
    qstt = pro.filter(title = sub)
    selpro = SalesmanProduct.objects.all()
    return render(request, 'product/detaile_product.html', {"qstt": qstt,"selpro":selpro, "pro":pro,"sub":sub})