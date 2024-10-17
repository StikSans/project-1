from django.urls import path
from django.shortcuts import render
from .views import register, login_view, logout_user, profile_view, settings_profile

urlpatterns = [
    path('auth/reg/', register, name='reg'),
    path('auth/login/', login_view, name='login'),
    path("auth/logout/", logout_user, name="logout"),
    path('profile/', profile_view, name="profile"),
    path("settings/", lambda req: render(req, "settings.html"), name='setting_profile'),
    path('settings/profile/', settings_profile, name="setting" )
]
