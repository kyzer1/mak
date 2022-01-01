from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView



def home_page(request):
    ctx = {}
    return render(request, 'index.html', ctx)

def category_header(request): # --> category haye header
    pass


def papular_category(request): #--> 3 dasteye por forosh
    pass


def new_products(request):
    pass


def most_sold_products(request): # --> por forosh tarin ha
    pass


def most_product_have_off(request):# --> category haei ke bishtarin tedade mahsole off khorde ra darad
    pass


def best_rated_store(request):# --> foroshgahi ke behtarin nomre ha ra gerefte ast
    pass


def best_offer(request): #--> bishtarin takhfie mahsolat
    pass


def offerable_products(request):#--> ba tavajoh be mahsolati ke karbar bishtar dide handle shavad
    pass


def brands(request):#--> brand haye site
    pass