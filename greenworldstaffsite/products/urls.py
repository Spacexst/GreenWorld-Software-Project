from django.contrib import admin
from django.urls import path
from .views import ProductList
from . import views

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    
]
