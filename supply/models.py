from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from product.models import Product, Property
from salesman_profile.models import SalesmanProfile

class SalesmanProduct(models.Model):
    salesman = models.ForeignKey(SalesmanProfile, related_name='salesmans', on_delete=models.CASCADE, null=True)
    # primary_product = models.ManyToManyField(PrimaryProduct, null=True)
    price = models.IntegerField(null=True)
    date_import_product = models.DateTimeField(auto_now_add=True, null=True)# add to intermadiate table
    date_last_update = models.DateTimeField(auto_now=True, null=True)# add to intermadiate table
    amount = models.BigIntegerField(null=True)#pas az sefaresh az in kam shavad
    product = models.ForeignKey(Product, related_name='products', on_delete=DO_NOTHING, null=True)
    


    def __str__(self) -> str:
        return f'{self.salesman}/ {self.product}'




class SalesManProperty(models.Model):
    salesman = models.ForeignKey(SalesmanProduct, related_name='salesproducts', on_delete=models.CASCADE, null=True)
    prop = models.ForeignKey(Property, related_name='props', on_delete=models.CASCADE, null=True)
   


    def __str__(self) -> str:
        return f"{self.prop.prop}:{self.salesman.product.title}:{self.salesman.salesman}"


class Property_Values(models.Model):
    prop=models.ForeignKey(SalesManProperty,on_delete=models.CASCADE,related_name="values")
    value=models.CharField(max_length=255)

    def __str__(self):
        return self.value