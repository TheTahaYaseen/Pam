from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home_view(request):
    page_title = "Home"
    context = {"page_title": page_title}
    return render(request, "home.html", context)

def register_view(request):
    page_title = "Register"
    form_action = page_title
    context = {"page_title": page_title, "form_action": form_action}
    return render(request, "auth_form.html", context)

def login_view(request):
    page_title = "Login"
    form_action = page_title
    context = {"page_title": page_title, "form_action": form_action}
    return render(request, "auth_form.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")
