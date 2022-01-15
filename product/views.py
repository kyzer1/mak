from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import CategoryProduct, Product
from django.views.generic import ListView


def show_sub_cat(request): # --> showing sub_cat after click 
    sub = []
    parent_category = CategoryProduct.objects.all().filter(parent=None)

    for cat in parent_category:
        sub.append(cat.child_cat.all())

    ctx = {
        'sub_category': sub
    }

    return render(request, 'product/sub_cat.html', ctx)


def show_sub_cat_det(request, cat): # --> showing sub_cat after click 
    sub = CategoryProduct.objects.filter(parent__title=cat)

    ctx = {
        'sub_category': sub
    }

    return render(request, 'product/sub_cat.html', ctx)


class ShowProductBySubCategory(ListView):
    template_name = 'product/detail_sub_cat.html'
    context_object_name ='products'
    paginate_by = 16


    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.all().filter(cat__title=kwargs.get('sub_cat'))
        return super().get(self, request, *args, **kwargs)



class ShowProductCategory(ListView):
    template_name = 'product/list_product_cat.html'
    context_object_name ='products'
    paginate_by = 16

    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.all().filter(cat__parent=kwargs.get('id'))
        return super().get(self, request, *args, **kwargs)


class ProductList(ListView):
    model = Product
    template_name = 'product/list_products.html'
    context_object_name ='products'
    paginate_by = 16

