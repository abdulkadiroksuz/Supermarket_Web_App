from django.urls import path
from .models import Category,Product
from .views import category,product

app_name = 'item'

urlpatterns = [
    path("category/<slug:category_slug>/", category, name="category"),
    path("product/<slug:product_slug>/", product, name="product"),
]