# django

from customer_profile.models import CustomerAddress, CustomerProfile
import redis
from django.shortcuts import get_object_or_404

# django rest
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, ProfileSerializer, ProfileAddressSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status



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


class ProfileDetail(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = ProfileAddressSerializer
    lookup_field = 'pk'

    def get(self, request, pk, format=None):
        queryset = CustomerAddress.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProfileAddressSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = ProfileAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdate(generics.UpdateAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = ProfileAddressSerializer