from django.template.loader import render_to_string
from customer_profile.models import CustomerProfile
from .forms import RegisterFormCustomer, LoginFormCustomer
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

def final_verification(subject, message, email_from, recipient_list):
    print("in send")
    send_mail( subject, message, email_from, recipient_list)



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
        return redirect('/')
    return render(request, 'customer_profile/customer_register.html', {'register_form': register_form})



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
            print(email)
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

            return redirect('/')