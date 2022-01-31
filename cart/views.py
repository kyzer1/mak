from django.shortcuts import render
import redis
from django.views.generic import ListView
from supply.models import SalesmanProduct
from customer_profile.models import CustomerProfile
from django.contrib.auth.decorators import login_required
import json


def show_cart(request):
    r=redis.Redis(decode_responses=True,encoding ="utf-8")
    if request.user.is_authenticated:
        key=request.user.email
    else:
        key=request.session.session_key
    print(f"key:{key}")
    data=r.hgetall(key)
    print(data)

    data_loads={}
    for k in data:
        data_loads[k] = json.loads(data[k])
    print('data_loads',data_loads)

    #To do : get data after pressing اعمال تغییرات سبد خرید
    l=request.POST.getlist("product_number")
    new_product_number=[]
    for i in l:
        new_product_number.append((int(i)))
    
    #clean and normalize data
    clean_data={}
    for i,j in data_loads.items():
        clean_data[i]=j
    
    result=0  
    for i,j in clean_data.items():
        result+=j[0]*j[2]
        
    ctx={"data":clean_data,"result":result,"new_product_number":new_product_number}
    new_product_number.clear()
    return render(request,"cart/base_cart.html",ctx)

@login_required(login_url='/customer_login/')
def order_summary(request):
    ctx={}
    r=redis.Redis(decode_responses=True,encoding ="utf-8")
    if request.user.is_authenticated:
        key=request.user.email
    else:
        key=request.session.session_key
    
    data=r.hgetall(key)
    data_loads={}
    for k in data:
        data_loads[k] = json.loads(data[k])
    print('data_loads',data_loads)

    #To do : get data after pressing اعمال تغییرات سبد خرید
    l=request.POST.getlist("product_number")
    new_product_number=[]
    for i in l:
        new_product_number.append((int(i)))
    
    #clean and normalize data
    clean_data={}
    for i,j in data_loads.items():
        clean_data[i]=j
    
    result=0  
    for i,j in clean_data.items():
        result+=j[0]*j[2]

    #Todo: account info
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