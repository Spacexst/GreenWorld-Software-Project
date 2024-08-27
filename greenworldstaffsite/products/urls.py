from django.contrib import admin
from django.urls import path
from .views import ProductList, StaffListView
urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path('staff/', StaffListView.as_view(), name='staff_list')
]
