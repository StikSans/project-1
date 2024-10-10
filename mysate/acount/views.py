from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import RegisterUser, LoginUser
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(req:HttpRequest):
    if req.method == 'POST':
        form = RegisterUser(req.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')
    else:
        form = RegisterUser()

    return render(req, 'register.html', {'form': form})


def login_view(req: HttpRequest):
    if req.method == 'POST':
        form = LoginUser(req, data=req.POST)
        if form.is_valid: 
            user = User.objects.get(username=req.POST['username'])
            if user is not None:
                if user.check_password(req.POST['password']):
                    login(req, user)
                    return redirect('home')
    
    form = LoginUser(req)
        
        
    return render(req, 'login.html', {'form': form})


def logout_user(req: HttpRequest):

    if req.method == 'POST':
        logout(req)
    
    return redirect('home')


@login_required(login_url='login')
def profile_view(req: HttpRequest):
    return render(req, 'profile.html', )