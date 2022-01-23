from product.models import CategoryProduct
from salesman_profile.models import User


def show_category(request):
    return {"p_category":list(CategoryProduct.objects.filter(parent__isnull=True))}

