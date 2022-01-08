from django.shortcuts import render


def products(request):
    ctx = {}
    return render(request, 'product/base_products.html', ctx)