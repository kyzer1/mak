from django.shortcuts import render
from django.views.generic import DetailView,ListView
from comment.forms import CommentForm
from product.models import Product
from comment.models import Comment

def products(request):
    ctx = {}
    return render(request, 'product/base_products.html', ctx)



class Detail_Product(DetailView):
    model=Product
    context_object_name_="product"
    template_name ="product/detaile_product.html"
    # slug_field = 'product_slug'
    # slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
         ctx=super().get_context_data(**kwargs)
         first=self.get_object().products.first()
         ctx["first"]=first
         l=first.salesproducts.all()
         for i in l:
             print(i.prop)
             print(i.value)
         
         ctx["l"]=l
        #  first.props.value
         ctx["sayer"]=self.get_object().products.all().exclude(salesman=first.salesman)
        # ctx["comments"]=self.get_object().comments.all()
        
         ctx["form"] =CommentForm()
         ctx["comments"] = self.get_object().product_comment.all()
         return ctx

