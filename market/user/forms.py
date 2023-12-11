from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from storage.models import Area
from django.forms import widgets

class UserLoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget = widgets.TextInput()
        self.fields["password"].widget = widgets.PasswordInput()
    
