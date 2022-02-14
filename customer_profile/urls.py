import imp
from django.urls import path, include
from .views import (registercustomer, customer_login, customerlogout, email_activate,
                        forget_password, forget_pass, set_true, checkForActivationMail, 
                            profilecustomer, my_address, my_comments)

from customer_profile.my_api.views import MyUserLoginTokenPairView, RegisterView, ProfileList, ProfileDetail, ProfileUpdate
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

app_name = 'customer_profile'

profile_update = ProfileList.as_view({
    'get': 'retrieve',
    'put': 'update'
})

router = DefaultRouter(trailing_slash=False)
router.register(r'customerapi', ProfileList)


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
    path('login-api/', MyUserLoginTokenPairView.as_view(), name='token_obtain_pair'),
    path('login-api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register-api/', RegisterView.as_view(), name='auth_register'),
    path('profile-api/<int:pk>/', profile_update, name='profile_api'),
    path('myprofile-api/<int:pk>/', ProfileDetail.as_view(), name='myprofile_api'),
    path('myprofile-api-up/<int:pk>/', ProfileUpdate.as_view(), name='ProfileUpdate')
]

urlpatterns += router.urls