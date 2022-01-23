from django.db import models
# from customer_profile.models import CustomerProfile
# from product.models import Product
from django.conf import settings
from supply.models import SalesmanProduct
 

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    salesman_product = models.ForeignKey(SalesmanProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.salesman_product}"

    def get_total_item_price(self):
        return self.quantity * self.salesman_product.price

    # def get_discount_item_price(self):
    #     return self.quantity * self.salesman_product.discount_price

    # def get_amount_saved(self):
    #     return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.salesman_product.price:        
            return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
