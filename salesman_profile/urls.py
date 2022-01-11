from django.urls import path
from .views import registersalesman, salesmanlogout, salesman_login, email_activate

app_name = 'salesman_profile'

urlpatterns = [
    path('registersalesman/', registersalesman, name='registersalesman'),
    path('salesmanlogout/', salesmanlogout, name='salesmanlogout'),
    path('salesman_login/', salesman_login, name='salesman_login'),
    path('email_activate/', email_activate, name='email_activate'),
]