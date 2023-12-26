from django.shortcuts import render

# Create your views here.
def create_view(request):
    form_action = "Create"
    page_title = f"{form_action} Task"
    context = {"page_title": page_title, "form_action": form_action}
    return render(request, "task_form.html", context) 

def update_view(request, primary_key):
    form_action = "Update"
    page_title = f"{form_action} Task"
    context = {"page_title": page_title, "form_action": form_action}
    return render(request, "task_form.html", context) 

def delete_view(request, primary_key):
    page_title = "Delete Task"
    context = {"page_title": page_title}
    return render(request, "delete.html", context) 

def tasks_view(request):
    page_title = "Tasks"
    context = {"page_title": page_title}
    return render(request, "tasks.html", context) 

def task_view(request, primary_key):
    page_title = "Task"
    context = {"page_title": page_title}
    return render(request, "task.html", context) 