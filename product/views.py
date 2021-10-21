from django.shortcuts import render
from .models import Product, ProductImages
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.views.generic.detail import DetailView
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here. 

class product_create(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product/product_create.html"
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        images = self.request.FILES.getlist("more_images")
        print("=========>>>", type(self.request.user))
        print("<<<=========>>>", type(form.instance.seller))
        p = form.save()
        for i in images:
            ProductImages.objects.create(product=p, image=i)
        return super().form_valid(form) 

class Product_list(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductList(ListView):
    model = Product
    template_name='product/product_list.html'
    context_object_name = 'context'
    print("-------->>>>>", type(context_object_name))
    def get_queryset(self):
        return Product.objects.filter(seller = self.request.user)


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
    context_object_name = 'product'

    def get_context_data(self,**kwargs):
        context = super(Product_detail, self).get_context_data(**kwargs)
        context['photos'] = ProductImages.objects.filter(photo_id=self.kwargs['pk'])
        return context

# class ImageUpdate(UpdateView):
#     model = ProductImages
#     form_class = ImageForm
#     template_name = 'product/images_create.html'   
#     success_url = '/'