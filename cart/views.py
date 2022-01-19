from itertools import product
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from product.models import Product

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.all()
            item = OrderItem.objects.all()
            print(order)
            title = []
            print(order, item)
            for elm in order.items.order_item.all():
                for item in elm.salesman_product.products.first():
                    title.append(item.product.title)
            
            print(title)

            context = {
                'order' : order
            }
            return render(self.request, 'cart/order_summary.html', context)
        except ObjectDoesNotExist:
            messages(self.request, "You do not have an order")
            return redirect("/")


def reduce_quantity_item(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("cart:order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("cart:order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("cart:order-summary")
