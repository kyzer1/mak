from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core import validators



User = get_user_model()

class RegisterFormCustomer(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار کلمه عبور خود را وارد نمایید'}),
        label='تکرار کلمه ی عبور'
    )


    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=username).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


# class RegisterFormCustomer(ModelForm):
#     re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control input-password', "id":"password"}))
#     class Meta:
#         model = CustomerProfile

        
#         fields = ['username','email','password']

#         widgets = {
#             'username': TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید', 'type':'text', 'class':'form-control'}),
#             'email': EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'class':'form-control'}),
#             'password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control', "id":"password"}),
#             're_password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'class':'form-control input-password', "id":"password"})
#         }

#         labels = {
#             'username' : _('user name or nick name'),
#             'email' : _('email'),
#             'password' : _('password'),
#             're_password' : _('re_password')
#         }

#         validators = {
#             'email' : EmailValidator('ایمیل وارد شده معتبر نمیباشد')
#         }
    
#     # def clean_email(self):
#     #     email = self.cleaned_data.get('email')
#     #     is_exists_user_by_email = User.objects.filter(email=email).exists()
#     #     if is_exists_user_by_email:
#     #         raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')

#     #     if len(email) > 20:
#     #         raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 20 باشد')

#     #     return email
    
#     def clean_username(self):
#         user_name = self.cleaned_data.get('username')
#         is_exists_user_by_username = User.objects.filter(username=user_name).exists()

#         if is_exists_user_by_username:
#             raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

#         return user_name

#     def clean_re_password(self):
#         password = self.cleaned_data.get('password')
#         re_password = self.cleaned_data.get('re_password')
#         print(password)
#         print(re_password)

#         if password != re_password:
#             raise forms.ValidationError('کلمه های عبور مغایرت دارند')

#         return password

#     def save(self, commit=True):
#         '''
#         override user create form to create profile after register!
#         '''
#         if self.is_valid():
#             username=self.cleaned_data['username']
#             email=self.cleaned_data['email']
#             password=self.cleaned_data['password']
#             user = CustomerProfile.objects.create_user(email=email,password=password,username=username,is_active=False)
#             return user
        


class LoginFormCustomer(forms.Form):
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

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'class':'form-control'}),
        label='ایمیل'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user = User.objects.filter(email=email).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با ایمیل وارد شده ثبت نام نکرده است')

        return email


class ForgetPassForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار کلمه عبور خود را وارد نمایید'}),
        label='تکرار کلمه ی عبور'
    )

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


class ProfileDetail(forms.Form):
    # name = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
    #     label='نام'
    # )


    # familyname = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
    #     label='نام خانوادگی'
    # )

    # email = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
    #     label='ایمیل',
    #     validators=[
    #         validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
    #     ]
    # )

    telephone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='تلفن'
    )


    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='موبایل'
    )


    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='آدرس'
    )


    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='کد پستی'
    )
