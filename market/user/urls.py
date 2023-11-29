# users_app/urls.py
from django.urls import path
from .views import loginView, signup, profile, logout_view

app_name = 'user'

urlpatterns = [   
    path('login/', loginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    # Add other URLs as needed
]
