from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate


def signup_request(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}

    return render(request, 'register.html', context)


def login_request(request):
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')

    context = {'form':form}

    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    return redirect('home')
