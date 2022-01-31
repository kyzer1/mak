from itertools import product
from unicodedata import name
from django.core.cache import cache
from django.shortcuts import redirect, render
import json
import redis
from django.views.generic import ListView
from supply.models import SalesmanProduct
from customer_profile.models import CustomerProfile
from django.contrib.auth.decorators import login_required
from payment.models import Payment
from customer_profile.models import CustomerProfile
from salesman_profile.models import SalesmanProfile
from supply.models import SalesmanProduct
from product.models import Product
from django.db.models import Q


def reduce_quantity_item(request):
    pass


def show_cart(request):
  
    r=redis.Redis(decode_responses=True,encoding ="utf-8")
    if request.user.is_authenticated:
            key=str(request.user.email)
    else:
            key=str(request.session._get_or_create_session_key())

    data=r.hgetall(key)
    clean_data={}

    #get data after pressing اعمال تغییرات سبد خرید
    l=request.POST.getlist("product_number")
    new_product_number=[]
    for i in l:
        new_product_number.append((int(i)))
    
    #clean and normalize data
    for i,j in data.items():
        j=j.strip('[]\"')
        j=j.split(',')
        j[1]=j[1].strip("\'")
        clean_data[i]=j
       
    result=0  
    for i,j in clean_data.items():
        j[0]=int(j[0].strip("'"))#product_number
        j[1]=j[1].strip("'")#img url
        j[2]=j[2].strip("'")
        j[2]=float(j[2].lstrip(" ' "))#price
        j[3]=j[3].strip("'")#salesman name
        j[4]=j[4].strip("'")#salesman id
        result+=j[0]*j[2]
        
    print(f"image: {j[1]}")
   

    ctx={"data":clean_data,"result":result,"new_product_number":new_product_number}
    new_product_number.clear()
    return render(request,"cart/base_cart.html",ctx)

@login_required(login_url='/customer_login/')
def order_summary(request):
    ctx={}
    r=redis.Redis(decode_responses=True,encoding ="utf-8")
    if request.user.is_authenticated:
            key=str(request.user.email)
    else:
            key=str(request.session._get_or_create_session_key())

    data=r.hgetall(key)
    clean_data={}
#clean and normalize data
    for i,j in data.items():
        
        j=j.strip('[]\"')
        j=j.split(',')
        j[1]=j[1].strip("\'")
        clean_data[i]=j
   
    
    result=0  
    for i,j in clean_data.items():
        j[0]=int(j[0].strip("'"))#product_number
        j[1]=j[1].strip("'")#img url
        j[2]=j[2].strip("'")
        j[2]=float(j[2].lstrip(" ' "))#price
        j[3]=j[3].strip("'")#salesman name
        j[4]=j[4].strip("'")#salesman id
        result+=j[0]*j[2]

    #account info
    if request.user.is_authenticated:
        first_name=request.user.first_name
        last_name=request.user.last_name
        email=request.user.email
        usr_obj=CustomerProfile.objects.get(email=email)
        addres=usr_obj.customer_ad.first()
        # postal_code=usr_obj.postal_code 
        ctx["first_name"]=first_name
        ctx["last_name"]=last_name
        ctx["email"]=email
        ctx["addres"]=addres

    ctx={"data":clean_data,"result":result}

    return render(request,"cart/order_summary.html",ctx)



def faktor(request):
    # final_price = request.session.get("jame_kol")
    user_id = request.user.id
    user_all = CustomerProfile.objects.all().values_list('id', flat=True)
    l_user = []
    for elm in user_all:
        l_user.append(elm)
    if user_id in l_user:
        r=redis.Redis(decode_responses=True,encoding ="utf-8")
        if request.user.is_authenticated:
                key=str(request.user.email)
        else:
                key=str(request.session._get_or_create_session_key())
        data=r.hgetall(key)
        clean_data={}
        #clean and normalize data
        for i,j in data.items():
            
            j=j.strip('[]\"')
            j=j.split(',')
            j[1]=j[1].strip("\'")
            clean_data[i]=j
        
        faktor = Payment()
        customer=CustomerProfile.objects.get(email=key)
        salesman = SalesmanProfile.objects.get(email="123@123.com")
        faktor.customer = customer
        # faktor.cart = data
        json_data=json.dumps(data)
        faktor.cart = json.loads(json_data)
        faktor.salesman = salesman
        faktor.save()
        result=0
        for i,j in clean_data.items():
            j[0]=int(j[0].strip("'"))#product_number
            j[1]=j[1].strip("'")#img url
            j[2]=j[2].strip("'")
            j[2]=float(j[2].lstrip(" ' "))#price
            j[3]=j[3].strip("'")#salesman name
            j[4]=j[4].strip("'")#salesman id
            b = j[3]
            sal_pro_object=SalesmanProduct.objects.filter(Q(product__title=i) & Q(salesman__username=b[2:]))
            result+=j[0]*j[2]
            for i in sal_pro_object:
                l = i.amount - j[0]
                if l >= 0:
                    i.amount = l
                else:
                    i.amount = 0
                i.save()

            for elm in sal_pro_object:
                Product.objects.filter(title=elm.product).update(sold_out_num=j[0])
                

        ctx={"data":clean_data,"result":result}


        return render(request, "cart/faktor.html", ctx)
    else:
        return redirect("home")