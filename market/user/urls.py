# users_app/urls.py
from django.urls import path
from .views import loginView, signupView,logoutView

app_name = 'user'

urlpatterns = [   
    path('login/', loginView.as_view(), name='login'),
    path('logout/', logoutView, name='logout'),
    path('signup/', signupView, name='signup'),
    # Add other URLs as needed
]
