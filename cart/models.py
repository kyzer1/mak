from django.db import models
from customer_profile.models import CustomerProfile
from product.models import Product

# from product.models import Product
from salesman_profile.models import SalesmanProfile


class Cart(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    salesman = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    count_order = models.BigIntegerField(null=True)
    is_paid = models.BooleanField(default=False, null=True)# zamani ke pardakht anjam shod True shavad va dar history vared shavad



class Order(Cart):
    date_order = models.DateTimeField(auto_now_add=True, null=True)
    expire_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.customer}  {self.salesman}'




class HistoryCustomer(Cart): # handle in view with query
    pass

    def __str__(self) -> str:
        return self.customer # name karbar bargandade shavd

