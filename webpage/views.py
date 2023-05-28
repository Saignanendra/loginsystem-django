from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if User.objects.filter(username=username):
            messages.error(request, "username already exist Please try some other username")
            return redirect('/signup')
        if User.objects.filter(email=email):
            messages.error(request, "email already registered!")
            return redirect('/signin')
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
        if not username.isalnum():
            messages.error(request, "username must be in Alpha-Numeric!")
            return redirect('/signup')
        if len(password) < 8:
            messages.error(request, "password must be greater than 8 characters and less than 16 characters")
            return redirect('/signup')
        if not password.isalnum():
            messages.error(request, "password must contain alpha-numeric!")
            return redirect('/signup')

        if password != confirm_password:
            messages.error(request, "password didn't match")

        user = User.objects.create_user(username=username,password=password)
        user.email = email
        user.save()

        messages.success(request, "your account has been successfully created ")
        return redirect('/signin')
    else:
       return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect('/')

        else:
            messages.error(request, "Invalid Details")
            return redirect('/signup')

    else:
      return render(request, 'signin.html')
def signout(request):
     logout(request)
     messages.success(request, "successfully logged out")
     return redirect('/')