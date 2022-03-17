from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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
        self.fields["email"].widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"Email", "autocomplete":"off"})


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields["username"].label="Your Username"
        self.fields["username"].widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username", "autocomplete": "off"})

        self.fields["password"].label="Your Password"
        self.fields["password"].widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"********", "autocomplete": "off", "data-toggle": "password"})
