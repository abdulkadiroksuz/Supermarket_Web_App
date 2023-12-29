from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer,Adress
from storage.models import Area
from django.forms import widgets
from django.db import transaction

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
    
    def save(self, commit=True):
        with transaction.atomic():
            user = super().save(commit=False)
            if commit:
                user.save()
            customer, created = Customer.objects.get_or_create(user=user)
            customer.phone = self.cleaned_data.get('phone')
            customer.area = self.cleaned_data.get('area')
            if commit:
                customer.save()

        return user
    


    
class UserPasswordChangeForm(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class": "form-control", 'placeholder': 'New Password'})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Confirm New Password'})
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Current Password'})


class AddressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['title', 'full_adress']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'full_adress': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Full Address'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddressForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        customer = cleaned_data.get('customer') or getattr(self.instance, 'customer', None)
        if customer is None and self.request:
            customer = self.request.user.customer

        if self.instance and self.instance.pk:
            if Adress.objects.exclude(pk=self.instance.pk).filter(customer=customer, title=title).exists():
                self.add_error('title', "There is an address with this title! Please enter a different title.")
        else:
            if Adress.objects.filter(customer=customer, title=title).exists():
                self.add_error('title', "There is an address with this title! Please enter a different title.")

        return cleaned_data