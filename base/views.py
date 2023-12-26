from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="login")
def home_view(request):
    page_title = "Home"
    context = {"page_title": page_title}
    return render(request, "home.html", context)

def register_view(request):
    page_title = "Register"
    form_action = page_title
    error = ""

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        if "" in [username, password]:
            error = "You cannot leave any field empty"
        elif len(password) < 8:
            error = "Password must be longer than 8 characters"
        else:
            try:
                user = User.objects.get(username=username)
                error = "User with username already exists"
            except User.DoesNotExist:
                user = User.objects.create(username=username, password=password)
                login(request, user)
                return redirect("home")

    context = {"page_title": page_title, "form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def login_view(request):
    page_title = "Login"
    form_action = page_title
    error = ""

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        if "" in [username, password]:
            error = "You cannot leave any field empty"
        else:
            try:
                user = User.objects.get(username=username, password=password)
                login(request, user)
                return redirect("home")
            except User.DoesNotExist:
                try:
                    user = User.objects.get(username=username)
                    error = "Incorrect credentials"
                except User.DoesNotExist:
                    error = "User with username doesn't exist"

    context = {"page_title": page_title, "form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")
