from django.urls import path
from .views import register

urlpatterns = [
    path('auth/reg/', register, name='reg')
]
