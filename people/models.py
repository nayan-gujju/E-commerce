from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class MyUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    customername = models.CharField(max_length=20, null=True) 
    sellername = models.CharField(max_length=20, null=False) 
    mobile = models.CharField(max_length=10)
    address1 = models.TextField(blank=False, null=True)
    address2 = models.TextField(blank=False, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    pin_code = models.CharField(blank=False, max_length=6, null=True)
    
    def __str__(self):
        return self.sellername

    def get_absolute_url(self):
        return reverse("home")

