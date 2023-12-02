# users_app/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import login, logout
from .forms import UserLoginForm, UserSignupForm, UserCreationForm
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


def signupView(request):
    areas = Area.objects.all()  # Retrieve all areas from the database

    if request.method == "POST":
        user_form = UserSignupForm(request.POST)
        profile_form = UserCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Log the user in after signing up
            login(request, user)

            return redirect("core:index")  # Redirect to the home page or any other page

    else:
        user_form = UserSignupForm()
        profile_form = UserCreationForm()

    return render(
        request,
        "user/signup.html",
        {"user_form": user_form, "profile_form": profile_form, "areas": areas},
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


def logoutView(request):
    logout(request)
    return redirect("core:index")
