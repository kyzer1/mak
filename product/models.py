from django.db import models
from django.db.models.deletion import SET_NULL
from salesman_profile.models import SalesmanProfile
from django.urls import reverse
# from cart.models import Order

# from customer_profile.models import HistoryCustomer



class CategoryProduct(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=SET_NULL, null=True, blank=True)
    # product = models.ForeignKey(Product, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.title

    def get_url(self):
        return reverse ('product:detail/',args=[self.pk])



class Property(models.Model):
    cat = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True)
    prop = models.CharField(max_length=255, verbose_name='properties')


    def __str__(self) -> str:
        return self.prop



# class PrimaryProduct(models.Model):
#     title = models.CharField(max_length=255, null=True)
#     cat = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True)



class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    img = models.ImageField(upload_to='product_media/', null=True, blank=True)
    img = models.ImageField(upload_to='product_media/', null=True, blank=True)
    img = models.ImageField(upload_to='product_media/', null=True, blank=True)
    img = models.ImageField(upload_to='product_media/', null=True, blank=True)
    active = models.BooleanField(default=True)
    date_prodcut = models.DateTimeField(auto_now=True)
    salesman = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True)
    sold_out_num = models.BigIntegerField(null=True)



    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):
        return reverse ('product:det_product',args=[self.pk])







    # img = models.ImageField(upload_to='product_media/', null=True, blank=True)
