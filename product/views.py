from django.shortcuts import render
from .models import Product 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import ProductForm

# Create your views here.


class product_create(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

class Product_list(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class Product_update(UpdateView):
    model = Product
    fields = ('title', 'price', 'discount_price', 'description', 'image')
    template_name = 'product/product_update.html'
    success_url = '/product/list'

class Product_delete(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = '/product/list'

class Product_detail(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = 'products'
    # pk_url_kwarg = "id"