from django.db import models
from django.db.models.deletion import DO_NOTHING

from customer_profile.models import CustomerProfile
from salesman_profile.models import SalesmanProfile

class Payment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomerProfile, related_name='customer_payment', on_delete=DO_NOTHING)
    salesman = models.ForeignKey(SalesmanProfile, related_name='salesman_payment', on_delete=DO_NOTHING)
    cart = models.JSONField()
