from django.contrib import admin
from product.models import CategoryProduct, Product, SubCategoryProduct

admin.site.register(CategoryProduct)
admin.site.register(SubCategoryProduct)
admin.site.register(Product)
