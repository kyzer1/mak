from django.contrib import admin

from supply.models import Property_Values, SalesManProperty, SalesmanProduct,Property_Values

admin.site.register(SalesmanProduct)
admin.site.register(SalesManProperty)
admin.site.register(Property_Values)

