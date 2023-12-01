# users_app/urls.py
from django.urls import path
from .views import loginView, signupView, profileView, logoutView

app_name = 'user'

urlpatterns = [   
    path('login/', loginView.as_view(), name='login'),
    path('signup/', signupView, name='signup'),
    path('profile/', profileView, name='profile'),
    path('logout/', logoutView, name='logout'),
    # Add other URLs as needed
]
