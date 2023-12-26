from django.urls import path

from . import views

urlpatterns = [
    path("", views.tasks_view, name="tasks"),
    path("<str:primary_key>", views.task_view, name="task"),
    path("create", views.create_view, name="create"),
    path("<str:primary_key>/update", views.update_view, name="update"),
    path("<str:primary_key>/delete", views.delete_view, name="delete"),
]
