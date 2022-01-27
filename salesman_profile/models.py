from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=11)
    date_joined = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'


class SalesmanProfile(User):
    telephone = models.CharField(max_length=11, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class SalesmanAddress(models.Model):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    salesman_id = models.ForeignKey(SalesmanProfile, related_name='salesman_ad', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.salesman_id} {self.address}'



# User.objects.create_user




