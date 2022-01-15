from typing import Any
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import CategoryProduct, Product
from django.views.generic import ListView
from comment.forms import CommentForm
from comment.models import Comment



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


class ShowProduct(ListView):
    template_name = 'product/detail_sub_cat.html'
    context_object_name ='products'
    paginate_by = 16

    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.all().filter(cat__title=kwargs.get('sub_cat'))
        return super().get(self, request, *args, **kwargs)


class Detail_Product(DetailView):
    model=Product
    context_object_name_="product"
    template_name ="product/detaile_product1.html"
    # slug_field = 'product_slug'
    # slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
         ctx=super().get_context_data(**kwargs)
         first=self.get_object().products.first()
         ctx["first"]=first
         if first:
            l=first.salesproducts.all()
            if l:
                ctx["l"]=l
            sayer=self.get_object().products.all().exclude(salesman=first.salesman)
            ctx["sayer"]=sayer
        
         ctx["form"] =CommentForm()
         ctx["comments"] = self.get_object().product_comment.all()
         category=self.get_object().cat
         same_cat=Product.objects.filter(cat=category).exclude(id=self.get_object().id)
         print(f"******{same_cat}")
         ctx["same_cat"]=same_cat
         return ctx






    