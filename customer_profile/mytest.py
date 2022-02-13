# # django 
# from profile import Profile
# from django.core.mail import send_mail
# from django.core.cache import cache
# from verification_email_token_gen import account_activation_token
# from customer_profile.models import CustomerAddress, CustomerProfile, User
# import redis

# # django rest
# from rest_framework import mixins
# from rest_framework import viewsets
# from .serializers import MyTokenObtainPairSerializer
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializers import RegisterSerializer, ProfileSerializer, ProfileAddressSerializer
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from drf_braces.mixins import MultipleSerializersViewMixin


# class MyUserLoginTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer



# class RegisterView(generics.CreateAPIView):
#     queryset = CustomerProfile.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer


# # class ProfileCreator(APIView):

# #     def get(self, request):
# #         queryset = CustomerProfile.objects.all()
# #         serializer = ProfileSerializer(queryset, many=True)
# #         return Response(serializer.data)

# #     def post(self, request, format=None):
# #         serializer1 = ProfileSerializer(data = request.data)
# #         serializer2 = ProfileAddressSerializer(data = request.data)

# #         if serializer1.is_valid():
# #             serializer1.create(flag=False)
# #             if serializer2.is_valid():
# #                 serializer1.create(flag=True)
# #                 serializer1.save()
# #                 serializer2.save()
# #                 return Response(serializer1.data, serializer2.data,status=status.HTTP_201_CREATED)
# #         return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

# # class ProfileCreator(generics.CreateAPIView ,MultipleSerializersViewMixin):
# #     queryset = CustomerProfile.objects.all()
# #     # serializer_class = [ProfileSerializer, ProfileAddressSerializer]

# #     serializer_class = ProfileSerializer

# #     def create(self, request, *args, **kwargs):
# #         serializer = self.get_serializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)

# #         saved = self.perform_create(serializer)
# #         serializer = self.get_serializer(instance=saved, serializer_class=ProfileAddressSerializer)

# #         headers = self.get_success_headers(serializer.data)
# #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# #     def perform_create(self, serializer):
# #         return serializer.save()


# # class ProfileCreator(generics.CreateAPIView, generics.UpdateAPIView):
# #     queryset = CustomerProfile.objects.all()
# #     # serializer_class = [ProfileSerializer, ProfileAddressSerializer]

# #     serializer_class = ProfileSerializer

# #     def create(self, request, *args, **kwargs):
# #         # return super().create(request, *args, **kwargs)
# #         user_id = request.user.id
# #         my_user= CustomerProfile.objects.filter(id= user_id)
# #         serializer = self.get_serializer(data=request.data)
# #         for info in my_user:
# #             if info.phone_number == None and info.telephone == None:
# #                 my_user.create()

# class ProfileCreator(generics.ListCreateAPIView):
#     queryset = CustomerProfile.objects.all()
#     serializer_class = ProfileSerializer
#     # permission_classes = [IsAccountAdminOrReadOnly]

#     # def put(self, request, id):
#     #     obj = CustomerProfile.objects.get(id=id)
#     #     serializer = ProfileSerializer(obj, data=request.data)
#     #     if serializer.is_valid():
#     #         ss = serializer.save(commit=False)
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request, id):
#     #     queryset = Tudo.objects.filter(id=id)
#     #     queryset.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)