from django.db import models
# from django.contrib.auth.models import User
from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerProfile(User):
    telephone = models.CharField(max_length=11, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self) -> str:
        return self.username



class CustomerAddress(models.Model):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    customer = models.ForeignKey(CustomerProfile, related_name='customer_ad', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.customer} {self.address}'



class Favotite(models.Model):
    user = models.ForeignKey(CustomerProfile, related_name='users', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_fav', on_delete=models.DO_NOTHING) # badan dar view handle shavad

