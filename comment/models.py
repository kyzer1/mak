from django.db import models
from customer_profile.models import CustomerProfile
# from salesman_profile.models import SalesmanProfile
from product.models import Product



class Comment(models.Model):
    rate_choices = [
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****')
    ]
    rate = models.CharField(max_length=50,choices=rate_choices, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, related_name='product_comment', on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfile, related_name='customers', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.comment
