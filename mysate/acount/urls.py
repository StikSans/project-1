from django.urls import path
from .views import register, login, logout_user

urlpatterns = [
    path('auth/reg/', register, name='reg'),
    path('auth/login/', login, name='login'),
    path("auth/logout/", logout_user, name="logout")
]
