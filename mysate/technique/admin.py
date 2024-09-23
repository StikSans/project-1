from django.contrib import admin
from .models.techique import Techique

@admin.register(Techique)
class Admin_Technique(admin.ModelAdmin):
    pass