from django.shortcuts import render, HttpResponse

# Create your views here.

def get_privet(request):
  return HttpResponse('<h1>Привет</h1>')