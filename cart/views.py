from django.shortcuts import render
import redis
from django.views.generic import ListView

class OrderSummaryView(ListView):
    pass 


def reduce_quantity_item(request):
    pass


def show_cart(request):
  
    r=redis.Redis(decode_responses=True)
    if request.user.is_authenticated:
            key=str(request.session["email"])
    else:
            key=str(request.session._get_or_create_session_key())
    data=r.hgetall(key)
    data1=dict()
#     print(data)
    keys=data.keys()
    values=data.values()
    print(data.items())

    for i,j in data.items():
        j=j.strip('[]\"')
        j=j.split(',')
        data1[i]=j
    print(data1.items())

    result=0  
    for i,j in data1.items():
        j[0]=int(j[0].strip("'"))
        j[1]=j[1].strip("'")
        j[2]=j[2].strip("'")
        j[2]=float(j[2].lstrip(" ' "))
        j[3]=j[3].strip("'")
        j[4]=j[4].strip("'")
        result+=j[0]*j[2]
        print(f"type j[0]{type(j[0])}")
        print(data1.items())

    
    

    ctx={"data":data1,"result":result}
    return render(request,"cart/base_cart.html",ctx)

