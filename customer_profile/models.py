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
    seller_id = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)



class Favotite(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=DO_NOTHING) # badan dar view handle shavad



class HistoryCustomer(models.Model): # handle in view with query
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    count_order = models.BigIntegerField()# dar view handle shavad
    date_order = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.customer # name karbar bargandade shavd