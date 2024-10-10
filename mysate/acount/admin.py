from django.contrib import admin
from acount.models import Profile
# Register your models here.


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass