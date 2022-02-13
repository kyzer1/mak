# django 

from nbformat import read
from customer_profile.models import CustomerProfile, CustomerAddress
from customer_profile.models import User

# drf

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from drf_braces.serializers.form_serializer import FormSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from customer_profile.views import ProfileDetail

# class UserLoginSerializer(serializers.ModelSerializer):
    
#     password = serializers.CharField(allow_blank=False)

#     class Meta:

#         model = CustomerProfile

#         fields = ['email', 'password']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True, required=True)

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomerProfile
        fields = ('username', 'password', 'password2', 'email')
        # extra_kwargs = {
        #     'email': {'required': True},
        #     'username': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "پسورد شما یکی نمیباشد !!"})

        return attrs

    def create(self, validated_data):
        user = CustomerProfile.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerProfile
        fields = ['telephone', 'phone_number']
    
    # def save(self, commit = True, **kwargs):
    #     usersave =  super().save(**kwargs)
    #     if commit:
    #         usersave.save()
    #     return usersave

    # def create(self, flag=None, *args, **kwargs):
    #     user_profile = CustomerProfile(*args, **kwargs)
    #     if flag == True:
    #         user_profile.save()    
    #         return user_profile
    #     else:
    #         return user_profile

class ProfileAddressSerializer(serializers.ModelSerializer):
    
    customer = serializers.RelatedField(many=True, read_only = True)

    class Meta:
        model = CustomerAddress
        fields = ['address', 'postal_code', "customer"]

# class ProfileSerializer(FormSerializer):
    
#     class Meta:
#         form = ProfileDetail