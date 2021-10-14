from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class CustomerForm(UserCreationForm):   
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = MyUser    
        fields = ['username', 'first_name', 'last_name', 'email','customername', 'mobile','address1', 'address2', 'city', 'state', 'pin_code']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_customer = True
    #     if commit:
    #         user.save()
    #     return user



class ShopForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email','sellername','mobile']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        if commit:
            user.save()
        return user
