from django.contrib import admin
from customer_profile.models import CustomerProfile, CustomerAddress, Favotite

admin.site.register(CustomerProfile)
admin.site.register(CustomerAddress)
# admin.site.register(HistoryCustomer)
admin.site.register(Favotite)