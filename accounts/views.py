from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.contrib import messages
from accounts.models import RegisteredUser
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        usertype = request.POST.get('usertype')
        college = request.POST.get('college')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_name = first_name+last_name+college
        user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=password)
        ruser = RegisteredUser(first_name=first_name, last_name=last_name, usertype=usertype, college=college, email=email, password=password, date=datetime.today())
        ruser.save()
        user.save()
        messages.success(request, 'Registration Success')
        return redirect('login')
    return render(request,'register.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        ruser = RegisteredUser.objects.filter(email=email)[0]
        if RegisteredUser.objects.filter(email=email).exists() and RegisteredUser.objects.filter(password=password).exists():
            username = ruser.first_name+ruser.last_name+ruser.college
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, 'Login Success')
                auth_login(request, user)
                print(user.first_name)
                return redirect('/')
            else:
                messages.warning(request, 'Email/Password Wrong')
        else:
            messages.warning(request, 'Email/Password Wrong')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged Out')
    return redirect('/')
def profile(request):
    return render(request, 'profile.html')
