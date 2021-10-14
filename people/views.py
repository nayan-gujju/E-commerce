from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from .forms import CustomerForm, ShopForm
# Create your views here.

class customer_register(CreateView):
    model = User
    form_class = CustomerForm
    template_name = 'people/customer_registration.html'

class shop_register(CreateView):
    model = User
    form_class = ShopForm
    template_name = 'people/shop_registration.html'

class Customer_profile(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email','customername', 'mobile','address1', 'address2', 'city', 'state', 'pin_code']
    template_name = 'people/customer_profile.html'
    success_url = '/'

class Shop_profile(UpdateView):
    model = User 
    fields = ['first_name', 'last_name', 'email','sellername', 'mobile']
    template_name = 'people/customer_profile.html'
    success_url = '/'