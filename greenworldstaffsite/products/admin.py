from django.contrib import admin
from .models import Product
from django.utils.html import format_html

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px;" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['name', 'image_tag']

admin.site.register(Product, ProductAdmin)

