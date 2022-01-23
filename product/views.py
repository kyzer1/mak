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
    



def add_to_cart(request,product_id):
    r=redis.Redis(decode_responses=True)
    if  request.method=="POST":
        product=request.POST.get("product")
        # request.session["product"]=product
        product_img=request.POST.get("product_img")
        # request.session["product_img"]=product_img
        product_number=request.POST.get("product_number")
        # request.session["product_number"]=product_number
        unit_price=request.POST.get("price")
        # request.session["price"]=price
        salesman_product_id=request.POST.get("salesman_product_id")
        # request.session["salesman_product_id"]=salesman_product_id
        salesman=request.POST.get("salesman")
        # request.session["salesman"]=salesman
        if request.user.is_authenticated:
            request.session["email"]=request.user.email
        request.session.save()
        list=str([product_number,product_img,unit_price,salesman,salesman_product_id])
        dict={product:list}
        if request.user.is_authenticated:
            key=str(request.session["email"])
        else:
            key=str(request.session._get_or_create_session_key())
            # print(f"sessin_key:{key}")
        r.hmset(key,mapping=dict)
        r.expire(key,1000)
        # print(r.hgetall(key))

        return redirect(reverse("products:detail_product",kwargs={"pk":product_id}))
        
