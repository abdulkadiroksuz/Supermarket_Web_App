from django.urls import path
from .models import Category,Product
from .views import category

app_name = 'item'

urlpatterns = [
    path("category/<slug:category_slug>/", category, name="category"),
]