from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from markupsafe import re
from salesman_profile.models import SalesmanProfile
from .forms import RegisterFormSalesman, ForgetPassForm, ForgetPasswordForm
from django.contrib.auth import login, authenticate, logout
import uuid
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from verification_email_token_gen import account_activation_token
from django.core.cache import cache
from django.conf import settings
from uuid import uuid4
from django.urls import reverse
from .models import User
from django.core import validators
from django import forms




def final_verification(subject, message, email_from, recipient_list):
    send_mail( subject, message, email_from, recipient_list)

def registersalesman(request):
    register_form = RegisterFormSalesman(request.POST or None)

    if register_form.is_valid():
        email = register_form.cleaned_data['email']
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        user = SalesmanProfile.objects.create_user(username=username, email=email, password=password, is_active=False, is_staff=False)
        cache.set('user',user, 200)
        current_site = get_current_site(request)
        uid = str(uuid.uuid1())
        cache.set('uid', uid, 120)
        subject = 'thank your for registering to mak store'
        message = render_to_string('customer_profile/vertification_mail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
        })
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [ email,]
        final_verification(subject, message, email_from, recipient_list)
        request.session['form'] = request.POST
        return redirect('/')
    return render(request, 'salesman_profile/salesmanregister.html', {'register_form': register_form})


# def email_activate(request):
#     register_form = RegisterFormSalesman(request.session['post'])
#     if request.method == 'GET':
#         return render(request, 'salesman_profile/emailshowbox.html', {})
#     elif request.method == 'POST':
#         if register_form.is_valid():
#             uid = request.POST.get('uid')
#             cache.set(uid, 120)
#             register_form.save(commit=True)
#             return redirect('/')

def email_activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = SalesmanProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, SalesmanProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_staff = True
        user.save()
        return render(request, 'salesman_profile/emailshowbox.html')
    else:
        return HttpResponse('Activation link is invalid!')



def salesmanlogout(request):
    logout(request)
    return redirect('/login')

# def salesman_login(request):
#     if request.user.is_authenticated:
#         return redirect('/')
    
#     login_form = LoginFormSalesman(request.POST or None)
#     if request.method == "GET":
#         context = {
#             'login_form': login_form
#         }
#         return render(request, 'salesman_profile/salesmanlogin.html', context)
#     elif request.method == "POST":
#         if login_form.is_valid():
#             email = login_form.cleaned_data.get('email')
#             password = login_form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

#             return redirect('/')    


def salesman_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "GET":
        return render(request, 'salesman_profile/loginsalesman.html', {})
    else:
        email = request.POST.get('email', "")
        password = request.POST.get("password", "")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')


def forget_password(request):
    forget_password_form = ForgetPasswordForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'salesman_profile/forget_password.html', {'forget_password_form': forget_password_form})

    elif request.method == "POST":
        if forget_password_form.is_valid():
            email = forget_password_form.cleaned_data.get("email")
            cache.set('email_miss',email,300)
            user = SalesmanProfile.objects.get(email=email)
            if user:
                uid = str(uuid.uuid1())
                cache.set('uid', uid, 120)
                current_site = get_current_site(request)
                subject = 'thank your for registering to mak store'
                message = render_to_string('salesman_profile/set_tru.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                })
                email_from = settings.EMAIL_HOST_USER

                recipient_list = [ email,]
                final_verification(subject, message, email_from, recipient_list)

                return redirect('/') # badan behesh ye message bede
            else:
                raise forms.ValidationError('همچین کاربری یافت نشد')


def set_true(request,uidb64 ,token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = SalesmanProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, SalesmanProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        return redirect('salesman_profile:forget_pass')
    else:
        return HttpResponse('Activation link is invalid!')


def forget_pass(request):
    forget_pass_form = ForgetPassForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'salesman_profile/forget_pass.html', {'forget_pass_form': forget_pass_form})
    elif request.method == "POST":
        print('in chache',cache.get('email_miss'))
        user = SalesmanProfile.objects.get(email=cache.get('email_miss'))
        if forget_pass_form.is_valid():
            password = request.POST.get("password", "")
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect("home")
        else:
            return redirect("salesman_profile:forget_password")