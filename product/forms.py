from django import forms
from .models import Product, Photos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'discount_price', 'description', 'image')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('image2','image3','image4','image5')