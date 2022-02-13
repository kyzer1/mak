# django 
from profile import Profile
from django.core.mail import send_mail
from django.core.cache import cache
from verification_email_token_gen import account_activation_token
from customer_profile.models import CustomerAddress, CustomerProfile, User
import redis

# django rest
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, ProfileSerializer, ProfileAddressSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_braces.mixins import MultipleSerializersViewMixin


class MyUserLoginTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = CustomerProfile.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class ProfileList(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = ProfileSerializer
