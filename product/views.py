from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import CategoryProduct, Product
from django.views.generic import ListView
from django.db.models import Q
from django.core.cache import cache
from supply.models import SalesmanProduct

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



class FilteringAll(ListView):
    model = SalesmanProduct
    template_name = 'product/side_bar_filtering.html'
    context_object_name = "productlist"
    paginate_by = 8

    def get_queryset(self):
        queryst =  super().get_queryset()
        filter_by_price_1 = self.request.GET.get("price1")
        filter_by_price_2 = self.request.GET.get("price2")
        if filter_by_price_1 and filter_by_price_2:
            queryst = SalesmanProduct.objects.filter(Q(price__gte=float(filter_by_price_2)) & Q(price__lte=float(filter_by_price_1)))
            cache.set('filtering_price', queryst, 5)
            # print("cache = ", queryst)
            # print(queryst)

            # for elm in queryst:
            #     print(elm.product.title)

            # print('my  query =====> ',queryst.get(product=Product.objects.get(id=3)))
        return queryst

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

    # def get_queryset(self):
    #     self.queryset = super().get_queryset()
    #     filtering_by_price = cache.get("filtering_price")

    #     # a = filtering_by_price.values(product=1)
    #     # print("cache:", filtering_by_price.all())
    #     # print(a in qs)        
    #     if filtering_by_price is None:
    #         self.queryset = Product.objects.all()
    #     else:
    #         self.queryset = filtering_by_price
    #         for elm in self.queryset:
    #             print(elm.product_id)
    #         # q = list(Product.objects.filter(products__id=filtering_by_price))
    #     return self.queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtering_by_price = cache.get("filtering_price")
        if filtering_by_price:
            my_dic = {}
            for elm in filtering_by_price:
                my_dic[elm.product.id]=elm.product
            context["my_products"] = my_dic.values
        else:
            pass
        return context
    
