from django.urls import path
from .views import register, login_view, logout_user, profile_view

urlpatterns = [
    path('auth/reg/', register, name='reg'),
    path('auth/login/', login_view, name='login'),
    path("auth/logout/", logout_user, name="logout"),
    path('profile/', profile_view, name="profile")
]
