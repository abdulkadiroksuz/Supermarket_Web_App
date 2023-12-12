# users_app/views.py
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, reverse
from storage.models import Area
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import UserLoginForm
from .models import Customer

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('core:index')  # Redirect to the desired page after login

        # If the form is not valid or the authentication failed
        messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return redirect('core:index')
 

""" def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', {'form': form})
 """

def user_logout(request):
    logout(request)
    return redirect("core:index")

    