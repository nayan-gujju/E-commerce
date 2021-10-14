from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Product 
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.views.generic.detail import DetailView
from .forms import ProductForm
from django.views.generic.base import View
# Create your views here.
# I have changed detail page and add functionlaity in demo project.
# I have learned One to Many Relationship model in django.
#I have learned math filters in django template language.
class product_create(View):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("=======", request.POST['image'])
        # print("--------", form['title'].value)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})        

# def show(request):
#     if request.method == 'POST':
#         fm = StudentInfo(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['name']
#             em = fm.cleaned_data['email']
#             pa = fm.cleaned_data['password']
#             print(nm)
#             print(em)
#             print(pa)
#             reg = User(name=nm, email=em, password=pa)
#             reg.save()
#     else:
#         fm = StudentInfo()

#     return render(request, 'enroll/home.html' , {'form':fm})

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
    context_object_name = 'product'