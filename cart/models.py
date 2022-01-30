from django.db import models
# from customer_profile.models import CustomerProfile
# from product.models import Product
from django.conf import settings
from supply.models import SalesmanProduct
 
class Order(models.Model):
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product=models.ForeignKey(SalesmanProduct,on_delete=models.CASCADE,related_name="orders")
    quantity = models.IntegerField(default=1)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_items")



