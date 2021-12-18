from django.db import models




class CategoryProduct(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class SubCategoryProduct(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='product_media/', null=True, blank=True)
    active = models.BooleanField(default=True)
    sub_category = models.ForeignKey(SubCategoryProduct, on_delete=models.CASCADE)
    date_prodcut = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


    