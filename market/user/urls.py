# users_app/urls.py
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [   
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('profile/',views.user_profile, name='profile'),
    # Add other URLs as needed
]
