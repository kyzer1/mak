from django.contrib import admin
from .models import CustomerProfile, CustomerAddress, HistoryCustomer, Favotite

admin.site.register(CustomerProfile)
admin.site.register(CustomerAddress)
admin.site.register(HistoryCustomer)
admin.site.register(Favotite)