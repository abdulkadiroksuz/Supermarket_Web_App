# users_app/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, reverse
from storage.models import Area

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


def profileView(request):
    customer = Customer.objects.get(user=request.user)
    areas = Area.objects.all()
    
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        area_name = request.POST.get('area')
        area = areas.get(name=area_name).id
        

        # Update customer information
        customer.name = name
        customer.surname = surname
        customer.email = email
        customer.phone = phone
        customer.area = area
        customer.save()

        # Redirect to the profile page after updating the customer
        return redirect('user:profile')
    
    context = {
        "logout_url": reverse("user:logout"),
        "customer": customer,
        "areas": areas,
        }
    return render(request, "user/profile.html", context)


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
