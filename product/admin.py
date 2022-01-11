from django.contrib import admin
from product.models import CategoryProduct, Product, Property
class ProductAdmin(admin.ModelAdmin):
    exclude=("product_slug",)


admin.site.register(CategoryProduct)
admin.site.register(Product,ProductAdmin)
admin.site.register(Property)

