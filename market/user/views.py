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
    if request.user.is_authenticated and "next" in request.GET:
        return render(request,"core:index", {"error":"Yetkiniz bulunmamaktadır."})

    if request.method == "POST":
        form = UserLoginForm(request,data=request.POST)
        if form.is_valid():     
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,"Giriş Başarılı")
                nextUrl = request.GET.get("next",None)
                if nextUrl is None:
                    return redirect("core:index")
                else:
                    return redirect(nextUrl)      
             
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

    