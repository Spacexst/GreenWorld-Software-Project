from django.urls import path
from .views import ProductList, product_management

urlpatterns = [
    path("products/", ProductList, name="product_list"),
    path('product/<int:product_id>/edit/',
         product_management, name='product_management'),
    ]
