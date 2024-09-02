from django.urls import path
<<<<<<< HEAD
from .views import ProductList, StaffList, product_management

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path('product/<int:product_id>/edit/',
         product_management, name='product_management'),
    path('staff/', StaffList.as_view(), name='staff_list'),
=======
from .views import ProductList
from . import views

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    
>>>>>>> a3b17b56d99f8bf8ceeb9d15814e3a3740c9159e
]
