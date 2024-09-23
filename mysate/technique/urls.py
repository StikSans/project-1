from django.urls import path
from .views import home_index, product, about, product_detail, search_product

urlpatterns = [
    path('home/', home_index, name='home'),
    path('product/', product, name='product'),
    path('abot/', about, name='about'  ),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('search_product/', search_product, name='search'),
]