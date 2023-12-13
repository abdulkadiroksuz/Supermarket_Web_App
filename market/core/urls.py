from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
    path("search/<slug:search_text>", views.search, name="search"),
    
   ]