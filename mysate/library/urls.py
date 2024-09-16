from django.urls import path
from .views import get_book, get_author

urlpatterns = [
  path('book/', get_book),
  path('author/', get_author)
]