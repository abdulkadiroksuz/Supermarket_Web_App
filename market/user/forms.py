from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Customer
from storage.models import Area
from django.forms import widgets

class UserLoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget = widgets.TextInput()
        self.fields["password"].widget = widgets.PasswordInput()


class SignUpForm(UserCreationForm):
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    area = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select','placeholder':'Select an area'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'area',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Boş seçeneği '--select an area--' metni ile değiştirin
        self.fields['area'].choices = [('', '--select an area--')] + [(area.id, area.name) for area in Area.objects.all()]


    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        # Example custom validation: Ensure email and phone are unique
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use.')
        if User.objects.filter(customer__phone=phone).exists():
            self.add_error('phone', 'This phone number is already in use.')

        return self.cleaned_data 


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            customer = Customer(user=user, phone=self.cleaned_data["phone"], area=self.cleaned_data["area"])
            customer.save()
        return user
   



class ProfileUpdateForm(UserChangeForm):
    phone = forms.CharField(
        max_length=20, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    area = forms.ModelChoiceField(
        queryset=Area.objects.all(), 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select an area'})
    )
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        max_length=254, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'area')

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['area'].empty_label = '--select an area--'

    def clean(self):      
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        user = self.instance
        if email and User.objects.filter(email=email).exclude(pk=user.pk).exists():
            self.add_error('email', 'This email is already in use.')

        if phone and Customer.objects.filter(phone=phone).exclude(user=user).exists():
            self.add_error('phone', 'This phone number is already in use.')

        return self.cleaned_data