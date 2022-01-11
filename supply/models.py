from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from product.models import Product, Property
from salesman_profile.models import SalesmanProfile

class SalesmanProduct(models.Model):
    salesman = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE, null=True,related_name="salesmans")
    # primary_product = models.ManyToManyField(PrimaryProduct, null=True)
    price = models.FloatField(null=True)
    date_import_product = models.DateTimeField(auto_now_add=True, null=True)# add to intermadiate table
    date_last_update = models.DateTimeField(auto_now=True, null=True)# add to intermadiate table
    amount = models.BigIntegerField(null=True)#pas az sefaresh az in kam shavad
    product = models.ForeignKey(Product, on_delete=DO_NOTHING, null=True,related_name="products")
    


    def __str__(self) -> str:
        return f'{self.salesman}/ {self.product}'




class SalesManProperty(models.Model):
    salesman = models.ForeignKey(SalesmanProduct, on_delete=models.CASCADE, null=True,related_name="salesproducts")
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, null=True,related_name="props")
    value = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.value


        