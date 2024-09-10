from django.urls import path

from library.views import index_library

urlpatterns = [
  path('library/', index_library)
]