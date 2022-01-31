from product.models import CategoryProduct
from salesman_profile.models import User


def show_category(request):
    if not request.session.session_key:#create session key for every user visiting site
        request.session.save()
    return {"p_category":list(CategoryProduct.objects.filter(parent__isnull=True))}

