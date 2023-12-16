"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path



urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("core.urls"), name="core"),
    path('admin/logout/', lambda request: redirect('user:logout', permanent=False)),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'), name="user"),
    path('item/', include('item.urls'), name="item"),
    path('cart/', include('cart.urls'), name="cart"),
    path('order/', include('order.urls'), name="order"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
