from django.contrib import admin

from salesman_profile.models import HistorySalesman, SalesmanAddress, SalesmanProduct, SalesmanProfile

admin.site.register(SalesmanProfile)
admin.site.register(SalesmanAddress)
admin.site.register(SalesmanProduct)
admin.site.register(HistorySalesman)


