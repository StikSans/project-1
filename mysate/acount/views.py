from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import RegisterUser


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