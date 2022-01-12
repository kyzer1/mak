


# def final_verification(subject, message, email_from, recipient_list):
#     send_mail( subject, message, email_from, recipient_list)


# class SalesmanRegister(CreateView):
#     template_name = "salesman_profile/salesmanregister.html"
#     success_url = reverse_lazy('salesman_login')
#     form_class = RegisterFormSalesman
#     # success_url = 'salesman_login/'

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         uid = str(uuid.uuid1())
#         cache.set(uid, 120)
#         self.uid = uid

#     def form_valid(self, request, form):
#         current_site = get_current_site(request)
#         email = form.cleaned_data['email']
#         form.save(commit=False)

#         subject = 'thank your for registering to mak store'
#         # message = f'welcome to our store your vertification code is : {uid}'
#         message = render_to_string('salesman_profile/vertification_mail.html', {
#             'domain' : current_site.domain,
#             'uid' : self.uid
#         })
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [ email,]
#         final_verification(subject, message, email_from, recipient_list)

#         if email_activate(self, request, self.uid):
#             form.save(commit=True)

#         return super().form_valid(form)



#     def email_activate(request, uid):
#         try:
#             uid = cache.get(uid)
#             print(uid)
#             user_username = request.user.username
#             user = User.objects.get(username=user_username)
#         except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#         if user is not None:
#             user.save()
            
#             return render(request, 'salesman_profile/emailshowbox.html', {})
#         else:
#             return HttpResponse('Activation link is invalid!')


#     # def get_success_url(self):
#     #     return 'salesman_login/'

    



# def salesmanlogout(request):
#     logout(request)
#     return redirect('/login')

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
#             print(email)
#             password = login_form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

#             return redirect('/')
