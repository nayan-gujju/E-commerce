from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("create/", views.product_create.as_view(), name='create'),
    path("update/<int:pk>/", views.Product_update.as_view(), name='update'),
    # path("photoupdate/<int:pk>/", views.ImageUpdate.as_view(), name='imagecreate'),
    path("list/", views.ProductList.as_view(), name='list'),
    path("delete/<int:pk>/", views.Product_delete.as_view(), name='delete'),
    path("detail/<int:pk>/", views.Product_detail.as_view(), name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)