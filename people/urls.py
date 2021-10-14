from django.urls import path
from .views import customer_register, shop_register, Customer_profile, Shop_profile

urlpatterns = [
    path('customer/',customer_register.as_view(), name='customer'),
    path('shop/',shop_register.as_view(), name='shop'),
    path('cutomer-profile/<int:pk>/',Customer_profile.as_view(), name='customer_profile'),
    path('shop-profile/<int:pk>/',Shop_profile.as_view(), name='shop_profile'),
    # path('cutomer-data',Customer.as_view(), name='customer_data'),
]