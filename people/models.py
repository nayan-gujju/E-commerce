from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    customername = models.CharField(max_length=20) 
    sellername = models.CharField(max_length=20) 
    mobile = models.CharField(max_length=10)
    address1 = models.TextField(blank=False)
    address2 = models.TextField(blank=False)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(blank=False, max_length=6)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("home")

