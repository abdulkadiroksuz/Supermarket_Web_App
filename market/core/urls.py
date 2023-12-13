from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
    path("get_footer/", views.load_footer, name="update_footer"),
   ]