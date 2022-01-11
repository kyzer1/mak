from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from product.models import Product
# from django.contrib.auth import get_user_model

# User = get_user_model()

class CustomerProfile(User):
    telephone = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.username



class CustomerAddress(models.Model):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE,related_name="customer_ad")

    def __str__(self) -> str:
        return f'{self.customer} {self.address}'



class Favotite(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE,related_name="users")
    product = models.ForeignKey(Product, on_delete=DO_NOTHING,related_name="product_fav") # badan dar view handle shavad

