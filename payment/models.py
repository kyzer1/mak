from django.db import models
from django.db.models.deletion import DO_NOTHING
from cart.models import Cart

from customer_profile.models import CustomerProfile
from salesman_profile.models import SalesmanProfile

class Payment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=DO_NOTHING)
    salesman = models.ForeignKey(SalesmanProfile, on_delete=DO_NOTHING)
    cart = models.JSONField()
