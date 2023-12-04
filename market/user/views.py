# users_app/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import login, logout
from .forms import UserLoginForm, SignUpForm
from .models import Customer
from storage.models import Area


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
