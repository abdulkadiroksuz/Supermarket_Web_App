# users_app/views.py
from django.contrib.auth import login, logout,authenticate,update_session_auth_hash
from django.shortcuts import redirect, render
from storage.models import Area
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm,ProfileUpdateForm,UserPasswordChangeForm,AddressForm
from .models import Customer,Adress

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.add_message(request,messages.SUCCESS,"Successfully logged in!")
                return redirect('core:index')  # Redirect to the desired page after login

        # If the form is not valid or the authentication failed
        messages.add_message(request,messages.ERROR,"Invalid username or password")

    else:
        form = AuthenticationForm()

    return redirect('core:index')
 

def user_signup(request):
    show_password_fields = True
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request,messages.SUCCESS,"Registration is successful!")
            login(request, user)
            return redirect('core:index')
        else:
            return render(request, 'user/signup.html', {'form': form,'show_password_fields' : show_password_fields})
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form,'show_password_fields' : show_password_fields})

def user_logout(request):
    messages.add_message(request,messages.SUCCESS,"Logged out!")
    logout(request)
    return redirect("core:index")


def user_profile(request):
    show_password_fields = False
    user = request.user
    password_form = UserPasswordChangeForm(user=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if "update_profile" in request.POST:
            if form.is_valid():
                user = form.save()  
                update_session_auth_hash(request, user)  
                messages.add_message(request,messages.SUCCESS, 'Your profile was successfully updated!')
                return redirect('user:profile') 
            else:
                return render(request, 'user/profile.html', {'form': form,'show_password_fields' : show_password_fields})
        elif "change_password" in request.POST:
            password_form = UserPasswordChangeForm(data=request.POST,user=user)
            if password_form.is_valid():
                updated_user = password_form.save()
                update_session_auth_hash(request, updated_user)
                messages.add_message(request, messages.SUCCESS, 'Your password was successfully updated!')
                return redirect('core:index')  
            else:
                user_data = {
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'phone': request.user.customer.phone if hasattr(request.user, 'customer') else '',
                    'area': request.user.customer.area if hasattr(request.user, 'customer') else '',
                }
                form = ProfileUpdateForm(initial=user_data)
    else:
        user_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone': request.user.customer.phone if hasattr(request.user, 'customer') else '',
            'area': request.user.customer.area if hasattr(request.user, 'customer') else '',
        }
        form = ProfileUpdateForm(initial=user_data)
    
    context = {
        'form': form,
        'password_form' : password_form,
        'show_password_fields':show_password_fields        
    }

    return render(request, 'user/profile.html',context)


def user_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.customer = request.user.customer
            address.save()
            messages.add_message(request,messages.SUCCESS,"Address is succesfully added!")
            return redirect('user:address')
    else:
        form = AddressForm()
    
    addresses = Adress.objects.filter(customer=request.user.customer)
    return render(request, 'user/address.html', {'addresses': addresses, 'form': form})