from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def create_view(request):
    form_action = "Create"
    page_title = f"{form_action} Task"
    context = {"page_title": page_title, "form_action": form_action}
    return render(request, "task_form.html", context) 

@login_required(login_url="login")
def update_view(request, primary_key):
    form_action = "Update"
    page_title = f"{form_action} Task"
    context = {"page_title": page_title, "form_action": form_action}
    return render(request, "task_form.html", context) 

@login_required(login_url="login")
def delete_view(request, primary_key):
    page_title = "Delete Task"
    context = {"page_title": page_title}
    return render(request, "delete.html", context) 

@login_required(login_url="login")
def tasks_view(request):
    page_title = "Tasks"
    context = {"page_title": page_title}
    return render(request, "tasks.html", context) 

@login_required(login_url="login")
def task_view(request, primary_key):
    page_title = "Task"
    context = {"page_title": page_title}
    return render(request, "task.html", context) 