from django.shortcuts import render
import redis
from django.views.generic import ListView
from supply.models import SalesmanProduct
from customer_profile.models import CustomerProfile
from django.contrib.auth.decorators import login_required


def reduce_quantity_item(request):
    pass


def show_cart(request):
  
    r=redis.Redis(decode_responses=True,encoding ="utf-8")
    if request.user.is_authenticated:
            key=str(request.user.email)
    else:
            key=str(request.session._get_or_create_session_key())
    print(f"key:{key}")
    print(f"session:{request.session}")
    data=r.hgetall(key)
    print(f"data:{data}")
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
    print(f"key:{key}")
    print(f"session:{request.session}")
    data=r.hgetall(key)
    print(f"data:{data}")
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