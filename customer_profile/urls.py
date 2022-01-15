from django.urls import path
from .views import registercustomer, customer_login, customerlogout, email_activate

app_name = 'salesman_profile'

urlpatterns = [
    path('registercustomer/', registercustomer, name='registercustomer'),
    path('customerlogout/', customerlogout, name='customerlogout'),
    path('customer_login/', customer_login, name='customer_login'),
    path('email_activate/<str:uidb64>/<str:token>', email_activate, name='email_activate'),
]