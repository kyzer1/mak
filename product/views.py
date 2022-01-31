from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from .models import CategoryProduct, Product
from django.views.generic import ListView
from django.db.models import Q
from django.core.cache import cache
from supply.models import SalesmanProduct
from comment.forms import CommentForm
from comment.models import Comment
from django.http import JsonResponse
from django.urls import reverse
import redis
import json




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



# class ShowProductBySubCategory(ListView):
#     template_name = 'product/detail_sub_cat.html'
#     context_object_name ='products'
#     paginate_by = 16


#     def get(self, request, *args, **kwargs):
#         self.queryset = Product.objects.all().filter(cat__title=kwargs.get('sub_cat'))
#         return super().get(self, request, *args, **kwargs)



class Detail_Product(DetailView):
    model=Product
    context_object_name_="product"
    template_name ="product/detaile_product.html"
    slug_field = 'slug_title'
    slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
         ctx=super().get_context_data(**kwargs)
         first=self.get_object().products.first()
         ctx["first"]=first
         print('first:',first)
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
         ctx["same_cat"]=same_cat
         

         return ctx



# class ShowProductCategory(ListView):
#     template_name = 'product/list_product_cat.html'
#     context_object_name ='products'
#     paginate_by = 16

#     def get(self, request, *args, **kwargs):
#         self.queryset = Product.objects.all().filter(cat__parent=kwargs.get('id'))
#         return super().get(self, request, *args, **kwargs)



class FilteringAll(ListView):
    model = SalesmanProduct
    template_name = 'product/side_bar_filtering.html'
    context_object_name = "productlist"
    paginate_by = 8

    def get_queryset(self):
        queryst =  super().get_queryset()
        filter_by_price_1 = self.request.GET.get("price1")
        filter_by_price_2 = self.request.GET.get("price2")
        if filter_by_price_1 is None and filter_by_price_2  is None:
            cache.set("filtering_price", [])
        else:
            cache.set("filtering_price", [filter_by_price_1, filter_by_price_2])
            queryst = SalesmanProduct.objects.filter(Q(price__gte=float(filter_by_price_2)) & Q(price__lte=float(filter_by_price_1)))
            cache.set('filtering_price', queryst)
        return queryst

    # def get_queryset(self):
    #     queryst =  super().get_queryset()

    #     return queryst

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_cat = CategoryProduct.objects.filter(parent__isnull=True)
        top_cat_2 = CategoryProduct.objects.filter(parent__isnull=False)
        context["category"] = top_cat
        context["sub_category"] = top_cat_2

        return context
    
    

class ProductList(ListView):
    model = Product
    template_name = 'product/list_products.html'
    context_object_name ='products'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.filter(cat__title=kwargs.get('category'))
        return super().get(self, request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(object_list=None ,**kwargs)
        filtering_by_price = cache.get("filtering_price")
        category = CategoryProduct.objects.filter(parent__isnull=True)
        context["category"] = category
        if filtering_by_price:
            my_dic = {}
            for elm in filtering_by_price:
                my_dic[elm.product.id]=elm.product
            context["my_products"] = my_dic.values

        return context
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(object_list=None ,**kwargs)
    #     category = CategoryProduct.objects.filter(parent__isnull=True)
    #     context["category"] = category

    #     return context
    



def add_to_cart(request, slug: str):
    r=redis.Redis()
    if  request.method=="POST":
        product=request.POST.get("product")
        product_img=request.POST.get("product_img")
        product_number=int(request.POST.get("product_number"))
        unit_price=int(request.POST.get("price"))
        salesman_product_id=int(request.POST.get("salesman_product_id"))
        salesman=request.POST.get("salesman")
        items_list=[product_number,product_img,unit_price,salesman,salesman_product_id]
        items_list=json.dumps(items_list)
        items_dict={product:items_list}
        if request.user.is_authenticated:
            key=request.user.email
            r.hset(key,mapping=items_dict)
            r.expire(key,300)#cart for 300 s remains in cache
        else:
            key=request.session.session_key
            r.hset(key,mapping=items_dict)
            r.expire(key,300)#cart for 300s remains in cache

        return redirect(reverse("products:detail_product",kwargs={"slug":slug}))
        
