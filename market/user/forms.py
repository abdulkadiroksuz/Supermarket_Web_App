from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Area, Customer

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Username',
        'id': 'login-username'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Password',
        'id': 'login-password'
    }))
    
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
    }))
    
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'phone', 'email', 'area']
        widgets = {
            'area': forms.Select(attrs={'class': 'form-control'}),
        }
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name',
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your last name',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your phone number',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
    }))