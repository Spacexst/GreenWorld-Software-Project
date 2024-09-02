from django.urls import path
from .views import ProductList, StaffList, product_management

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path('product/<int:product_id>/edit/',
         product_management, name='product_management'),
    path('staff/', StaffList.as_view(), name='staff_list'),
]
