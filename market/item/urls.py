from django.urls import path
from .views import category,product,get_categories

app_name = 'item'

urlpatterns = [
    path("category/<slug:category_slug>/", category, name="category"),
    path("product/<slug:product_slug>/", product, name="product"),
    path("get_categories", get_categories, name="get_categories")
]