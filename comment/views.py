from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from comment.forms import CommentForm
from django.core.exceptions import ValidationError
from .models import Comment
from django.urls import reverse
from django.contrib.auth import get_user_model
from product.models import Product
from customer_profile.models import CustomerProfile


# Create your views here.
User = get_user_model()


@login_required()#login_url
def add_comment(request,product_id):
    user_id = request.user.id
    user = CustomerProfile.objects.get(id=user_id)
    if request.method=="POST":
        form=CommentForm(request.POST)
        product=get_object_or_404(Product,pk=product_id)
        if form.is_valid():
            comment=form.cleaned_data.get("comment")
            rate=form.cleaned_data.get("rate")
            comment=Comment(customer=user,comment=comment,rate=rate ,product=product)
            comment.save()
            return redirect(reverse("products:detail_product",kwargs={"pk":product.id}))
        else:
            comments=product.product_comment.all()
            ctx={
                "form":form,
                "comments":comments,
                "product":product

            }

            return render(request,"product/detaile_product.html",ctx)

    