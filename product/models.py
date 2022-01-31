from django.db import models
from django.db.models.deletion import SET_NULL
from salesman_profile.models import SalesmanProfile
from django.utils.text import slugify
# from cart.models import Order

# from customer_profile.models import HistoryCustomer



class CategoryProduct(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='child_cat', on_delete=SET_NULL, null=True, blank=True)
    img = models.ImageField(upload_to='static/img', null=True, blank=True)
    # product = models.ForeignKey(Product, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.title



class Property(models.Model):
    cat = models.ForeignKey(CategoryProduct, related_name='cats', on_delete=models.CASCADE, null=True)
    prop = models.CharField(max_length=255, verbose_name='properties')


    def __str__(self) -> str:
        return self.prop



# class PrimaryProduct(models.Model):
#     title = models.CharField(max_length=255, null=True)
#     cat = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True)



class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    img1 = models.ImageField(upload_to='product_media/', null=True, blank=True)
    img2= models.ImageField(upload_to='product_media/', null=True, blank=True)
    img3 = models.ImageField(upload_to='product_media/', null=True, blank=True)
    img4 = models.ImageField(upload_to='product_media/', null=True, blank=True)
    active = models.BooleanField(default=True)
    date_prodcut = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(CategoryProduct, related_name='category', on_delete=models.CASCADE, null=True)
    sold_out_num = models.BigIntegerField(blank=True,default=0)
    slug_title=models.SlugField(blank=True,allow_unicode=True)

    def save(self,*args,**kwargs):
        # if not self.slug_title:
        self.slug_title=slugify(self.title,allow_unicode=True)
        super().save(*args,**kwargs)


    def __str__(self) -> str:
        return self.title








    # img = models.ImageField(upload_to='product_media/', null=True, blank=True)
