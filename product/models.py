from django.db import models
from django.urls import reverse
from people.models import MyUser
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
    
class Photos(models.Model):
    titlephoto = models.ForeignKey(Product, on_delete=models.CASCADE)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True) 