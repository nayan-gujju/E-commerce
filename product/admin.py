from django.contrib import admin
from .models import Photos, Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'seller','discount_price', 'description', 'image')

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id','image2','image3','image4','image5')
