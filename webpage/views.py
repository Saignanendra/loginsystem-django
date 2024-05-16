from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import User1, Student

from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

# Rest API Practice

class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer    

def home(request):

    students = Student.objects.all()

    if request.method == "POST":

        if "add" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')

            Student.objects.create(
                name = name,
                email = email
            )
            messages.success(request, "Student added successfully")


        elif "update" in request.POST:

            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')

            update_student = Student.objects.get(id=id)
            update_student.name = name
            update_student.email = email
            update_student.save()

            messages.success(request, "Student Updates successfully")

        elif "delete" in request.POST:

            id = request.POST.get('id')

            Student.objects.get(id=id).delete()

            messages.success(request, "Student Deleted successfully")

        elif "search" in request.POST:

            query = request.POST.get("searchquery")  
            students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))  

        
 



    context = {
           "students":students,
    }
    return render(request, 'home.html', context=context)


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

        user = User.objects.create_user(username=username, password=password)
        user1 = User1.objects.create(username=username, password=password, email=email)
        user1.save()
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
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect('/')

        else:
            messages.error(request, "Invalid Details")
            return redirect('/signup')

    else:
        return render(request, 'signin.html')


def sign_out(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect('/')
