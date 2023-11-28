# users_app/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from .forms import UserLoginForm


class loginView(LoginView):
    form_class = UserLoginForm
    template_name = "user/login.html"  # Specify your template path

    def form_valid(self, form):
        super().form_valid(form)
        # Customize the redirect destination based on user roles or conditions
        return redirect("admin:index") if self.request.user.is_staff else redirect("")

class logoutView(LogoutView):
    def get_next_page(self):
        # Customize the next page after logout (redirect to home in this example)
        return '/'

class signupView(LoginView):
    form_class = UserLoginForm
    template_name = "user/signup.html"  # Specify your template path
