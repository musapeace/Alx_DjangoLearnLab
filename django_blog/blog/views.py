from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserChangeForm

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    
    return render(request, "blog/register.html", {"form": form})

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("blog-home")
    else:
        form = AuthenticationForm()
    
    return render(request, "blog/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("login")

# User Profile View
def profile_view(request):
    return render(request, "blog/profile.html", {"user": request.user})



def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "blog/edit_profile.html", {"form": form})
