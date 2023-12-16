

# users_app/urls.py
from django.urls import path
from . import views
from .views import showDetail,listOrders    

app_name = 'order'

urlpatterns = [   
    path('order-history/', listOrders, name='order-history'),
    path('detail/<int:order_id>',showDetail,name='order-detail')
    # Add other URLs as needed
]
