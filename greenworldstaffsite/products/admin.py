from django.contrib import admin
from .models import User, Product, Staff

# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Staff)

