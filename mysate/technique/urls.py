from django.urls import path
from .views import home_index, product, about

urlpatterns = [
    path('home/', home_index, name='home'),
    path('product/', product, name='product'),
    path('abot/', about, name='about'  )
]