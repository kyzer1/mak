from django.urls import path
from .views import registersalesman, salesmanlogout, salesman_login, email_activate, forget_password, forget_pass, set_true

app_name = 'salesman_profile'

urlpatterns = [
    path('registersalesman/', registersalesman, name='registersalesman'),
    path('salesmanlogout/', salesmanlogout, name='salesmanlogout'),
    path('salesman_login/', salesman_login, name='salesman_login'),
    path('email_activate/<str:uidb64>/<str:token>', email_activate, name='email_activate'),
    path('forget_password/', forget_password, name='forget_password'),
    path('forget_pass/', forget_pass, name='forget_pass'),
    path("set_true/<str:uidb64>/<str:token>", set_true, name="set_true")    
]

