from django.db import models

# Create your models hefrom django import db
from django.db import models
from django.contrib.auth.models import User

from product.models import Product
# from django.contrib.auth import get_user_model

# User = get_user_model()

class SalesmanProfile(User):
    telephone = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    Product = models.ManyToManyField(Product)
    count = models.BigIntegerField()


    def __str__(self) -> str:
        return self.username


class SalesmanAddress(models.Model):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    seller_id = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE)



class HistorySalesman(models.Model): # handle in view with query
    salesman = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    count_order = models.BigIntegerField()# dar view handle shavad
    date_order = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.customer # name karbar bargandade shavd



class SalesmanProduct(models.Model):
    salesman = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_import_product = models.DateTimeField(auto_now_add=True)# add to intermadiate table
    date_last_update = models.DateTimeField(auto_now=True)# add to intermadiate table


