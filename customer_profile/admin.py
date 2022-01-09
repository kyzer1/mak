from django.contrib import admin
from .models import CustomerProfile, CustomerAddress, Favorite

admin.site.register(CustomerProfile)
admin.site.register(CustomerAddress)
# admin.site.register(HistoryCustomer)
admin.site.register(Favorite)