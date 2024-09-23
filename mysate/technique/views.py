from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.urls import reverse
from .models.techique import Techique
from django.db.models import Q





def home_index(req: HttpRequest):
    return render(req, 'home.html')


def product(req: HttpRequest):
    product = Techique.objects.all()
    return render(req, 'product.html', {'product': product})

def about(req: HttpRequest):
    return render(req, 'about.html')



def product_detail(req: HttpRequest, pk: int):
    product = Techique.objects.get(pk=pk)
    return render(req, 'product_detail.html', {'product': product})


def search_product(req: HttpRequest):
    if req.method == 'GET':
        search = req.GET['search']
        product = Techique.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return render(req, 'product.html', {'product': product})
    
    else:
        return redirect('home')
