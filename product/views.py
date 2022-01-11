from django.shortcuts import render
from .models import CategoryProduct, Product


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


def show_product(request, sub_cat):
    product = Product.objects.all().filter(cat__title=sub_cat)

    ctx = {
        'product': product
    }

    return render(request, 'product/detail_sub_cat.html', ctx)

    