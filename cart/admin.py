from django.contrib import admin
from .models import Cart, HistoryCustomer, Order

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(HistoryCustomer)

