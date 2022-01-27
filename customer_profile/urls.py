from django.urls import path
from .views import registercustomer, customer_login, customerlogout, email_activate, forget_password, forget_pass, set_true, checkForActivationMail, profilecustomer, my_address, my_comments

app_name = 'customer_profile'

urlpatterns = [
    path('registercustomer/', registercustomer, name='registercustomer'),
    path('customerlogout/', customerlogout, name='customerlogout'),
    path('customer_login/', customer_login, name='customer_login'),
    path('email_activate_customer/<str:uidb64>/<str:token>', email_activate, name='email_activate_customer'),
    path('checkForActivationMail/', checkForActivationMail, name='checkForActivationMail'),
    path('forget_password_customer/', forget_password, name='forget_password_customer'),
    path('forget_pass_customer/', forget_pass, name='forget_pass_customer'),
    path("set_true_customer/<str:uidb64>/<str:token>", set_true, name="set_true"),
    path("profilecustomer/", profilecustomer, name="profilecustomer"),
    path("my_address/", my_address, name="my_address"),
    path("my_comments/", my_comments, name="my_comments"),
]