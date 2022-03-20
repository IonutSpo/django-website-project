from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django.core.validators import RegexValidator
from datetime import date
from duishela_site import settings





class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields["username"].label = "Username"
        self.fields["username"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Username", "autocomplete":"off"})

        self.fields["password1"].label = "Password"
        self.fields["password1"].widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"********", "autocomplete": "off", "data-toggle": "password"})

        self.fields["password2"].label = "Confirm your password"
        self.fields["password2"].widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"********", "autocomplete": "off", "data-toggle": "password"})

        self.fields["first_name"].label = "First Name"
        self.fields["first_name"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name", "autocomplete":"off"})

        self.fields["last_name"].label = "Last Name"
        self.fields["last_name"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name", "autocomplete":"off"})

        self.fields["email"].label = "Email"
        self.fields["email"].widget = forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email", "autocomplete":"off"})


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):

    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)


    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Must be at least 18 years old to register')
        return dob


    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        self.fields["address"].label = "Address"
        self.fields["address"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Address", "autocomplete":"off"})

        self.fields["personal_number"].label = "Personal Numeric Code"
        self.fields["personal_number"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Personal Numeric Code", "autocomplete":"off"})

        self.fields["phone_number"].label = "Phone Number"
        self.fields["phone_number"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"+407", "autocomplete":"off"})

        self.fields["date_of_birth"].label = "Date Of Birth"
        self.fields["date_of_birth"].widget = forms.DateInput(attrs={"class":"form-control","placeholder":"d/m/y", "autocomplete":"off"})

    class Meta:
        model = ProfileModel
        fields = ("personal_number", "date_of_birth", "phone_number", "address")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields["username"].label="Your Username"
        self.fields["username"].widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username", "autocomplete": "off"})

        self.fields["password"].label="Your Password"
        self.fields["password"].widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"********", "autocomplete": "off", "data-toggle": "password"})


class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        self.fields["username"].label = "Username"
        self.fields["username"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Username", "autocomplete":"off"})

        self.fields["password"].label = "Password"
        self.fields["password"].widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"********", "autocomplete": "off", "data-toggle": "password"})

        self.fields["email"].label = "Email"
        self.fields["email"].widget = forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email", "autocomplete":"off"})

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        self.fields["address"].label = "Address"
        self.fields["address"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Address", "autocomplete":"off"})

        self.fields["phone_number"].label = "Phone Number"
        self.fields["phone_number"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"+407", "autocomplete":"off"})

    class Meta:
        model = ProfileModel
        fields = ("phone_number", "address")
