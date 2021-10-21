from django.contrib import admin
from .models import ProductImages, Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','price', 'seller','discount_price', 'description', 'image')

@admin.register(ProductImages)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id','image')
