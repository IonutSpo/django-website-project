from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProfileModel
from .forms import UserRegistrationForm, LoginForm, ProfileForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import login, logout, authenticate


# Signup / Login / Logout / UserDashboard (profile_details)
def signup_request(request):
    user_form = UserRegistrationForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.instance.user = user
            profile_form.save()

            messages.success(request, "Registered Succesfuly.")
            return redirect('login')

    context = {'user_form':user_form,
                'profile_form':profile_form}

    return render(request, 'register.html', context)


def login_request(request):
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Succesfuly.")
            return redirect('main')
        else:
            messages.error(request, "Username or Password not found")

    context = {'form':form}

    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    return redirect('home')


def profile_details(request):

    user = request.user
    profile = ProfileModel.objects.all()

    context = {'user':user, 'profile':profile}

    return render(request, 'profile.html', context)


# Update / Delete User Profile
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()
            messages.success(request, "Profile Updated Succesfuly.")

            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        user_form = UpdateUserForm(request.POST)
        profile_form = UpdateProfileForm(request.POST)

    context = {'user_form':user_form, 'profile_form':profile_form}

    return render(request, 'update_profile.html', context)


def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Profile Deleted Succesfuly.")
    return redirect('home')
