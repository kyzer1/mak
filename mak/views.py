from decimal import Context
from typing import Any, Dict
from django.db.models.aggregates import Avg, Max
from django.db.models.base import Model
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from product.models import CategoryProduct, Product
from salesman_profile.models import User

def home_page(request): #--> 3 dasteye por forosh --> hatman badan handle shavad
    popular_categories = list(CategoryProduct.objects.all().order_by('id')[:4])
    all_categoris = list(CategoryProduct.objects.all().order_by('id')[:3])
    most_sold_out = Product.objects.all().order_by('-sold_out_num')[:10]
    # all_products = list(Product.objects.all())
    # average_sold_out = list(Product.objects.all().aggregate(Avg('sold_out_num')))
    all_categoris_header = CategoryProduct.objects.all()
    parent_category = CategoryProduct.objects.all().filter(parent=None)
    new_products = Product.objects.all().order_by('-date_prodcut')[:10]


    sub = []

    for cat in parent_category:
        sub.append(cat.child_cat.all())

    ctx = {
        'popular_categories': popular_categories,
        'all_categories': all_categoris,
        'most_sold_out': most_sold_out,
        'all_categoris_header': all_categoris_header,
        'new_products': new_products,
        'parent_cat': parent_category,
        'sub_cat': sub,
    }
    
    return render(request, 'index.html', ctx)


# def header(request):
#     user_id = request.user.id
#     user = User.objects.get(id=user_id)
#     print(user)
#     # top_cat = CategoryProduct.objects.filter(parent__isnull=True)
#     # # print(top_cat)
#     # top_cat_2 = CategoryProduct.objects.filter(parent__isnull=False)
#     # # print(top_cat_2)
#     context = {
#         "user_profiles" : user
#         # "category" : top_cat, 
#         # "sub_category": top_cat_2
#     }
  
#     return render(request, 'header.html', context)


def PapularCategorie(request): 
    
    pass
    


def new_products(request):
    pass


def most_sold_products(request): # --> por forosh tarin ha
    pass


def most_product_have_off(request):# --> category haei ke bishtarin tedade mahsole off khorde ra darad
    pass


def best_rated_store(request):# --> foroshgahi ke behtarin nomre ha ra gerefte ast
    pass


def best_offer(request): #--> bishtarin takhfie mahsolat
    pass


def offerable_products(request):#--> ba tavajoh be mahsolati ke karbar bishtar dide handle shavad
    pass


def brands(request):#--> brand haye site
    pass