from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse("home")
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pia")
    image = models.ImageField(upload_to='products/images/', blank=True) 

    class Meta:
        verbose_name_plural = 'Photo'

    def __str__(self):
        return self.product.title