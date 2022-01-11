from django.http.response import Http404
from django.shortcuts import redirect, render
from .forms import RegisterFormSalesman, LoginFormSalesman
from django.contrib.auth import login, authenticate, logout
import uuid
from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings


def final_verification(subject, message, email_from, recipient_list):
    send_mail( subject, message, email_from, recipient_list)

def registersalesman(request):

    register_form = RegisterFormSalesman(request.POST or None)

    if register_form.is_valid():
        email = register_form.cleaned_data['email']
        register_form.save(commit=False)
        uid = str(uuid.uuid1())
        cache.set(uid, 120)
        subject = 'thank your for registering to mak store'
        message = f'welcome to our store your vertification code is : {uid}'

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [ email,]
        final_verification(subject, message, email_from, recipient_list)
        request.session['post'] = request.POST
        return redirect('salesman_profile:email_activate')

    return render(request, 'salesman_profile/salesmanregister.html', {'register_form': register_form})


def email_activate(request):
    register_form = RegisterFormSalesman(request.session['post'])
    if request.method == 'GET':
        return render(request, 'salesman_profile/emailshowbox.html', {})
    elif request.method == 'POST':
        if register_form.is_valid():
            uid = request.POST.get('uid')
            cache.set(uid, 120)
            request.session['0'] = uid
            register_form.save(commit=True)
            return redirect('/')


def salesmanlogout(request):
    logout(request)
    return redirect('/login')

def salesman_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    login_form = LoginFormSalesman(request.POST or None)
    if request.method == "GET":
        context = {
            'login_form': login_form
        }
        return render(request, 'salesman_profile/salesmanlogin.html', context)
    elif request.method == "POST":
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

            return redirect('/')    