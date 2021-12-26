from django.db import models
from django.db import models
from django.contrib.auth.models import User

class SalesmanProfile(User):
    telephone = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.username


class SalesmanAddress(models.Model):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    seller_id = models.ForeignKey(SalesmanProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.seller_id} {self.address}'








