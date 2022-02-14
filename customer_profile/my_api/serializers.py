# django 

from customer_profile.models import CustomerProfile, CustomerAddress
from customer_profile.models import User

# drf

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



from customer_profile.views import ProfileDetail



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
    

class ProfileAddressSerializer(serializers.ModelSerializer):
    
    customer = ProfileSerializer()

    class Meta:
        model = CustomerAddress
        fields = ['address', 'postal_code', 'customer']

    def create(self, validated_data):
        customer_data = validated_data.get('customer')
        datas = []
        for data in customer_data.items():
            datas.append(data[1])

        
        my_c, creating = CustomerProfile.objects.get_or_create(phone_number = datas[0], telephone=datas[1]) # bar ax dari mizni ddsh

        address = validated_data.pop('address')
        postal_code = validated_data.pop('postal_code')

        address_creating= CustomerAddress.objects.create(address=address, postal_code=postal_code, customer=my_c)


        return address_creating

    def update(self, instance, validated_data):
        customer_validated_data = validated_data.pop('customer', None)
        customer = instance.customer
        customer.phone_number = customer_validated_data.get('phone_number', customer.phone_number)
        customer.telephone = customer_validated_data.get('telephone', customer.telephone)
        customer.save()
        instance.address = validated_data.get('address', instance.address)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()
        return instance

