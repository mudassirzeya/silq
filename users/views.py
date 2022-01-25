import json
from django.core import serializers
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .forms import CompanyForm, RegisterForm
from .password import PasswordSet
from .models import UserProfile, Company
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
# from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

# template email sent
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

# reset email
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail, BadHeaderError
from django import template

# Create your views here.


def admin_registration(request):
    form1 = CompanyForm()
    form2 = RegisterForm()
    if request.method == 'POST':
        form2 = RegisterForm(request.POST)
        # print("form2: ", form2)
        form1 = CompanyForm(request.POST)
        # print("form1: ", form1)
        username = request.POST.get('email')
        print("username: ", username)
        if form2.is_valid():
            # print("form2 valid")
            newuser_obj = form2.save(commit=False)
            # print("form2: ", newuser_obj)
            newuser_obj.username = username
            newuser_obj.save()
            if form1.is_valid():
                # print("form1 valid")
                company_obj = form1.save(commit=False)
                company_obj.super_user = newuser_obj
                company_obj.save()
                UserProfile.objects.create(
                    user=newuser_obj,
                    company=company_obj,
                    user_type='admin',
                )
                return redirect('login')
        else:
            print("form2 not valid")
            return render(request, 'signup.html')
    context = {"form1": form1, "form2": form2}
    return render(request, 'signup.html', context)


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            userProfile = UserProfile.objects.get(user=request.user)
            usertype = userProfile.user_type
            company_name = userProfile.company
            superuser = company_name.super_user
            if request.user == superuser:
                return redirect('admin_page')
            elif usertype == 'customer':
                return redirect('customer_page')
            elif usertype == 'staff':
                return redirect('team_member_page')
        else:
            messages.info(request, 'Username or Password is in correct')
    context = {}
    return render(request, 'login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


def add_new_staff(request):
    loggedin_user = Company.objects.get(super_user=request.user)
    company = loggedin_user.company_name
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        passcode = PasswordSet()
        new_user = User.objects.create_user(
            username=email, password=passcode)
        new_user.email = email
        new_user.first_name = name
        new_user.save()
        UserProfile.objects.create(
            user=new_user,
            company=loggedin_user,
            user_type='staff',
        )

        msg_html = render_to_string('add_staff_email.html',
                                    {'first_name': name, 'company': company, 'username': email, 'password': passcode})
        text_content = strip_tags(msg_html)

        email = EmailMultiAlternatives(
            # title
            f'Mail From {company} admin',

            # context
            text_content,

            # from email
            settings.EMAIL_HOST_USER,

            # to email
            [email],
        )
        email.attach_alternative(msg_html, "text/html")
        email.send()
        return redirect('my_team')

    context = {}
    return render(request, 'admin_page.html', context)


def add_new_customer(request):
    loggedin_user = Company.objects.get(super_user=request.user)
    company = loggedin_user.company_name
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        passcode = PasswordSet()
        new_user = User.objects.create_user(
            username=email, password=passcode)
        new_user.email = email
        new_user.first_name = name
        new_user.save()
        UserProfile.objects.create(
            user=new_user,
            company=loggedin_user,
            user_type='customer',
        )

        msg_html = render_to_string('add_customer_email.html',
                                    {'first_name': name, 'company': company, 'username': email, 'password': passcode})
        text_content = strip_tags(msg_html)

        email = EmailMultiAlternatives(
            # title
            f'Mail From {company} admin',

            # context
            text_content,

            # from email
            settings.EMAIL_HOST_USER,

            # to email
            [email],
        )
        email.attach_alternative(msg_html, "text/html")
        email.send()
        return redirect('my_customers')

    context = {}
    return render(request, 'admin_page.html', context)
