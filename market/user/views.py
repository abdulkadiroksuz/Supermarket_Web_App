# users_app/views.py
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, reverse
from storage.models import Area
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, UserLoginForm
from .models import Customer


class loginView(LoginView):
    form_class = UserLoginForm
    template_name = "user/login.html"  # Specify your template path

    def form_valid(self, form):
        super().form_valid(form)
        # Customize the redirect destination based on user roles or conditions
        return (
            redirect("admin:index")
            if self.request.user.is_staff
            else redirect("core:index")
        )




def signupView(request):
    areas = Area.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            area = form.cleaned_data['area']

            customer = Customer.objects.create(
                user=user,
                name=name,
                surname=surname,
                email=email,
                phone=phone,
                area=area
            )

            return redirect('core:index')  
    else:
        form = SignUpForm()

    context = {
        'form': form,
        'areas': areas
    }
    return render(request, 'user/signup.html', context)

def logoutView(request):
    logout(request)
    return redirect("core:index")


def login_view(request):
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
        #messages.error(request, 'Invalid username or password.')
        
    else:
        form = AuthenticationForm()
    
    return redirect('core:index')