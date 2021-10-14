from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=False)

    def get_absolute_url(self):
        return reverse("home")
    