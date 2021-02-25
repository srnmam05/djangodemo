from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout

def Index(request):
    assert isinstance(request,HttpRequest)
    return render(request,'Index.html')

def crawlPage(request):
    return render(request,'crawl.html')

def login_(request):
    form = RegisterForm()

    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')

    context = {
        'form':form
    }

    return render(request,'login.html',context)

def Signin(request):

    form = LoginForm()
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    context = {
        'form':form
    }

    return render(request,'signin.html',context)

def logout_(request):

    logout(request)
    return redirect('/')