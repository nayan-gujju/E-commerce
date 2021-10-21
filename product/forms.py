from django import forms
from .models import Product, ProductImages

class ProductForm(forms.ModelForm):
    
    more_images = forms.FileField(required=False, widget=forms.FileInput(
        attrs={
            "class": 'form-control',
            "multiple": True,
        }
    ))

    class Meta:
        model = Product
        fields = ('title', 'price', 'discount_price', 'description', 'image')
        widgets = {
            "title":forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Enter the product title here..."
            })
        }
