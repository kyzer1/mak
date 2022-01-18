from product.models import CategoryProduct

def show_category(request):
    return {"p_category":list(CategoryProduct.objects.filter(parent__isnull=True))}