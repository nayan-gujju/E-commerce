from django import forms
from .models import Product
from people.models import MyUser
import requests
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'discount_price', 'description', 'image')