from django.http.response import HttpResponse
from django.shortcuts import redirect, render
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
        print(user)
        if user is not None:
            login(request, user)
        return redirect('/')


def forget_password(request):
    forget_password_form = ForgetPasswordForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'salesman_profile/forget_password.html', {'forget_password_form': forget_password_form})

    else:
        
        if forget_password_form.is_valid():
            miss_email=forget_password_form.cleaned_data.get('email')
            #user = authenticate(request, email=miss_email)
            user = User.objects.get(email=miss_email)
            # print(user)
            if user:
                uid=str(uuid4())
                # link=reverse("user:set_true",kwargs={"auten":uid})
                link=reverse("salesman_profile:set_true",kwargs={"auten":uid, "token":account_activation_token.make_token(user)})
                current_site = get_current_site(request)
                mail_subject = 'click on the link for change password.'
                message = "127.0.0.1:8000"+link
                print(message)
                to_email = forget_password_form.cleaned_data.get('email')
                # forget= f'{to_email}+flag'
                # request.session["forget"]=forget
                request.session["email"]=to_email
                cache.set("email1", to_email, 120)
                print(request.session.get("email"))
                request.session["uid"]=uid
                cache.set("uid1",uid,120)
                cache.set(to_email,uid,300)
                cache.set("forget",0,300)

                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

                # return redirect('/')
                return redirect('salesman_profile:forget_pass')

            else:
                return redirect('salesman_profile:forget_password')


    # if register_form.is_valid():
    #     email = register_form.cleaned_data['email']
    #     username = register_form.cleaned_data.get('username')
    #     password = register_form.cleaned_data.get('password')
    #     user = SalesmanProfile.objects.create_user(username=username, email=email, password=password, is_active=False, is_staff=False)
    #     cache.set('user',user, 200)
    #     current_site = get_current_site(request)
    #     uid = str(uuid.uuid1())
    #     cache.set('uid', uid, 120)
    #     subject = 'thank your for registering to mak store'
    #     message = render_to_string('customer_profile/vertification_mail.html', {
    #             'user': user,
    #             'domain': current_site.domain,
    #             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #             'token': account_activation_token.make_token(user),
    #     })
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = [ email,]
    #     final_verification(subject, message, email_from, recipient_list)
    #     request.session['form'] = request.POST
    #     return redirect('/')


def set_true(request,auten ,token):
    try:
        auten = cache.get("uid1")
        user = SalesmanProfile.objects.get(pk=auten)
    except(TypeError, ValueError, OverflowError, SalesmanProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        return redirect('salesman_profile:forget_pass')
    else:
        return HttpResponse('Activation link is invalid!')


    # try:
    #     uid = urlsafe_base64_decode(uidb64)
    #     user = SalesmanProfile.objects.get(pk=uid)
    # except(TypeError, ValueError, OverflowError, SalesmanProfile.DoesNotExist):
    #     user = None
    # if user is not None and account_activation_token.check_token(user, token):
    #     user.is_active = True
    #     user.is_staff = True
    #     user.save()
    #     return render(request, 'salesman_profile/emailshowbox.html')
    # else:
    #     return HttpResponse('Activation link is invalid!')

def forget_pass(request):
    forget_pass_form = ForgetPassForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'salesman_profile/forget_pass.html', {'forget_pass_form': forget_pass_form})
    
    else:
        user=SalesmanProfile.objects.get(email=request.session.get("email"))
        ucode=cache.get(request.session.get("email"))
        if request.session.get("uid")==ucode:
                forg=cache.get("forget")
                if forg:
                    if forget_pass_form.is_valid():
                        password = request.POST.get("password", "")
                        user.set_password(password)
                        user.save()

                        login(request,user)
                        return redirect("home")
                    else:
                        return redirect("user:forget_password")
                else:
                    return HttpResponse("bayad montazer email bashid..!")

        else:
            return HttpResponse("link taiid eshtebah ast...!")