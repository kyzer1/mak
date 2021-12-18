from django.db import models
from customer_profile.models import CustomerProfile

from product.models import Product
from salesman_profile.models import SalesmanProfile

class Order(models.Model):
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    salesman = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(auto_now=True)
    count_order = models.BigIntegerField()
    is_paid = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.id