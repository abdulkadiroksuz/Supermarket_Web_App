# users_app/views.py
from django.contrib.auth import login, logout,authenticate,update_session_auth_hash
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
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
    context = {'form_errors': False}
    form = AddressForm()
    addresses = Adress.objects.filter(customer=request.user.customer)
    context['addresses'] = addresses

    if request.method == 'POST':
        address_id = request.POST.get('address_id')

        if 'add_address' in request.POST:
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.customer = request.user.customer
                address.save()
                messages.success(request, "Address has been added successfully!")
                return redirect('user:address')

        elif 'edit_address' in request.POST:
            address = get_object_or_404(Adress, pk=address_id, customer=request.user.customer)
            form = AddressForm(request.POST, instance=address)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,"Address has been updated successfully!")
                return redirect('user:address')
            else:
                context['form_errors'] = True
                context['edit_address_id'] = address_id

        elif 'delete_address' in request.POST and address_id:
            address = get_object_or_404(Adress, pk=address_id, customer=request.user.customer)
            if address.customer != request.user.customer:
                return HttpResponseForbidden()
            address.delete()
            messages.add_message(request,messages.SUCCESS,"Address has been deleted successfully!")
            return redirect('user:address')

    else:
        form = AddressForm()

    context['form'] = form
    return render(request, 'user/address.html', context)