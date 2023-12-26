from django.shortcuts import render

# Create your views here.
def create_view(request):
    page_title = "Create Project"
    context = {"page_title": page_title}
    return render(request, "create_project.html", context) 

def update_view(request, primary_key):
    page_title = "Update Project"
    context = {"page_title": page_title}
    return render(request, "update_project.html", context) 

def delete_view(request, primary_key):
    page_title = "Delete Project"
    context = {"page_title": page_title}
    return render(request, "delete.html", context) 

def projects_view(request):
    page_title = "Projects"
    context = {"page_title": page_title}
    return render(request, "projects.html", context) 

def project_view(request, primary_key):
    page_title = "Project"
    context = {"page_title": page_title}
    return render(request, "project.html", context) 