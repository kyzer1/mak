from django.contrib import admin

from salesman_profile.models import SalesmanAddress, SalesmanProfile

admin.site.register(SalesmanProfile)
admin.site.register(SalesmanAddress)