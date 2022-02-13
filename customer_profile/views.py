from itertools import product
from django.template.loader import render_to_string
from markupsafe import re
from customer_profile.models import CustomerProfile, CustomerAddress
from product.models import Product
from .forms import RegisterFormCustomer, LoginFormCustomer,  ForgetPassForm, ForgetPasswordForm, ProfileDetail
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
import uuid
from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from verification_email_token_gen import account_activation_token
from .models import User
from django.core import validators
from django import forms
from django.contrib.auth.decorators import login_required
from comment.models import Comment
import redis
from .tasks import send_email_task


def final_verification(subject, message, email_from, recipient_list):
    # send_mail( subject, message, email_from, recipient_list)
    send_email_task(subject, message, email_from, recipient_list)



def registercustomer(request):
    register_form = RegisterFormCustomer(request.POST or None)

    if register_form.is_valid():
        email = register_form.cleaned_data['email']
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')

        user = CustomerProfile.objects.create_user(username=username, email=email, password=password, is_active=False)
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
        return redirect('customer_profile:checkForActivationMail')
    return render(request, 'customer_profile/customer_register.html', {'register_form': register_form})


def checkForActivationMail(request):
    return render(request, 'customer_profile/email_okbox.html')




def email_activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = CustomerProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomerProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'customer_profile/emailshowbox.html')
    else:
        return HttpResponse('Activation link is invalid!')


def customerlogout(request):
    logout(request)
    return redirect('customer_profile:customer_login')



def customer_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    login_form = LoginFormCustomer(request.POST or None)
    
    if request.method == "GET":
        context = {
            'login_form': login_form
        }
        return render(request, 'customer_profile/customer_login.html', context)
    elif request.method == "POST":
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                r=redis.Redis()
                try:
                    key=request.session.session_key
                    cart=r.hgetall(key)
                    r.hset(email,mapping=cart)
                except:
                    pass
                login(request, user)
                return redirect('/')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

            return redirect('/')

        else:#if user already not register
            print(f"error:{login_form.errors}")
            return redirect('customer_profile:registercustomer')


def forget_password(request):
    forget_password_form = ForgetPasswordForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'customer_profile/forget_password.html', {'forget_password_form': forget_password_form})

    elif request.method == "POST":
        if forget_password_form.is_valid():
            email = forget_password_form.cleaned_data.get("email")
            cache.set('email_miss',email,300)
            user = CustomerProfile.objects.get(email=email)
            if user:
                uid = str(uuid.uuid1())
                cache.set('uid', uid, 120)
                current_site = get_current_site(request)
                subject = 'thank your for registering to mak store'
                message = render_to_string('customer_profile/set_tru.html', {
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
        user = CustomerProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomerProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        return redirect('customer_profile:forget_pass_customer')
    else:
        return HttpResponse('Activation link is invalid!')


def forget_pass(request):
    forget_pass_form = ForgetPassForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'customer_profile/forget_pass.html', {'forget_pass_form': forget_pass_form})
    elif request.method == "POST":
        user = CustomerProfile.objects.get(email=cache.get('email_miss'))
        if forget_pass_form.is_valid():
            password = request.POST.get("password", "")
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect("home")
        else:
            return redirect("customer_profile:forget_password_customer")

# login required
def profilecustomer(request):
    user_id = request.user.id
    user_all = CustomerProfile.objects.all().values_list('id', flat=True)
    l_user = []
    for elm in user_all:
        l_user.append(elm)
    if user_id in l_user:
        user = CustomerProfile.objects.get(id=user_id)
        form = ProfileDetail(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                # name = form.cleaned_data.get("name")
                # familyname = form.cleaned_data.get("familyname")
                # email = form.cleaned_data.get("email")
                telephone = form.cleaned_data.get("telephone")
                phone_number = form.cleaned_data.get("phone_number")
                address = form.cleaned_data.get("address")
                postal_code = form.cleaned_data.get("postal_code")

                CustomerProfile.objects.update(telephone=telephone, phone_number=phone_number)
                a = CustomerAddress()
                a.address = address
                a.postal_code = postal_code
                a.customer = user
                a.save()
                return redirect('customer_profile:profilecustomer')

        return render(request, 'customer_profile/account-details.html', {"form" : form})
    else:
        return redirect("home")


def my_address(request):
    user_id = request.user.id
    user_all = CustomerProfile.objects.all().values_list('id', flat=True)
    l_user = []
    print(Comment.objects.filter(customer__id=user_id).values('product__id'))
    for elm in user_all:
        l_user.append(elm)
    if user_id in l_user:
        customer_profile = CustomerProfile.objects.filter(id=user_id).values_list('phone_number', flat=True)
        my_phone = list(customer_profile)
        customer_address = CustomerAddress.objects.filter(customer__id=user_id)
        return render(request, 'customer_profile/account-address.html', {'customer_number': my_phone[0], 'customer_addresss':customer_address})
    else:
        return redirect("home")


def my_comments(request):
    user_id = request.user.id
    user_all = CustomerProfile.objects.all().values_list('id', flat=True)
    l_user = []
    for elm in user_all:
        l_user.append(elm)
    if user_id in l_user:
        my_comment = Comment.objects.filter(customer__id=user_id)
        if request.method == "GET":
            context = {
                'my_comments' : my_comment,
            }
            return render(request, 'customer_profile/account-comments.html', context)
        elif request.method == "POST":
            cm_del = request.POST.get('cm_delete')
            delete_cm = Comment.objects.filter(id=cm_del)
            delete_cm.delete()
            return redirect("customer_profile:my_comments")
    else:
        return redirect("home")
