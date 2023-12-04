from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from storage.models import Area

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
    
class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True)
    surname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    area = forms.ModelChoiceField(queryset=Area.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'surname', 'email', 'phone', 'area']
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        # Example custom validation: Ensure email and phone are unique
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use.')
        if User.objects.filter(profile__phone=phone).exists():
            self.add_error('phone', 'This phone number is already in use.')

        return cleaned_data