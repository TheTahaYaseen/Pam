from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def create_view(request):
    page_title = "Create Project"
    context = {"page_title": page_title}
    return render(request, "create_project.html", context) 

@login_required(login_url="login")
def update_view(request, primary_key):
    page_title = "Update Project"
    context = {"page_title": page_title}
    return render(request, "update_project.html", context) 

@login_required(login_url="login")
def delete_view(request, primary_key):
    page_title = "Delete Project"
    context = {"page_title": page_title}
    return render(request, "delete.html", context) 

@login_required(login_url="login")
def projects_view(request):
    page_title = "Projects"
    context = {"page_title": page_title}
    return render(request, "projects.html", context) 

@login_required(login_url="login")
def project_view(request, primary_key):
    page_title = "Project"
    context = {"page_title": page_title}
    return render(request, "project.html", context) 