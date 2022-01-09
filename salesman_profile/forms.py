from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm, widgets, TextInput, EmailInput, PasswordInput
from django.core.validators import EmailValidator 
from .models import SalesmanProfile
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email',
                  'password1', 'password2']
        labels = {
            "email": "ایمیل",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",

        }

        help_texts = {
            "email": "ایمیل خود را به درستی وارد کنید",
        }

    def save(self, commit=True):
        '''
        override user create form to create profile after register!
        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()

        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name')


class RegisterFormSalesman(ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control input-password', "id":"password"}))
    class Meta:
        model = SalesmanProfile

        
        fields = ['username','email','password']

        widgets = {
            'username': TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید', 'type':'text', 'class':'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'class':'form-control'}),
            'password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control', "id":"password"}),
            're_password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control input-password', "id":"password"})
        }

        # labels = {
        #     'username' : _('user name or nick name'),
        #     'email' : _('email'),
        #     'password' : _('password'),
        #     're_password' : _('re_password')
        # }

        labels = {
            'username' : 'نام کاربری',
            'email' : 'ایمیل',
            'password' : 'رمز عبور',
            're_password' : 'تکرار رمز عبور'
        }

        validators = {
            'email' : EmailValidator('ایمیل وارد شده معتبر نمیباشد'),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')

        if len(email) > 20:
            raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 20 باشد')

        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

        return user_name
    
    # def save(self) :
    #     if self.is_valid():
            
    #         self.cleaned_data.pop('re_password')
    #         SalesmanProfile.objects.create(**self.cleaned_data)
    
    # def clean_password(self):
    #     pas=self.cleaned_data['password']
    #     pas #8ragham harf
    #     return pas
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


class LoginFormSalesman(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'class':'form-control'}),
        label='ایمیل'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control', "id":"password"}),
        label='کلمه ی عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user = User.objects.filter(email=email).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')

        return email
