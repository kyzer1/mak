from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import redirect, render
from django.urls.conf import include
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .forms import RegisterFormSalesman, LoginFormSalesman
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.http import HttpResponse



def registersalesman(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    register_form = RegisterFormSalesman()


    if request.method == "GET":
        return render(request, 'salesman_profile/salesmanregister.html', {'register_form': register_form})
    elif request.method == "POST":
        register_form = RegisterFormSalesman(request.POST)

        if register_form.is_valid():
            print(register_form.cleaned_data['email'])
            register_form.save()
            return redirect('/')
        return render(request, 'salesman_profile/salesmanregister.html', {'register_form': register_form})


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
            print(email)
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

            return redirect('/')