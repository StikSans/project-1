from django.shortcuts import render
from django.http import HttpRequest
from .models.techique import Techique




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