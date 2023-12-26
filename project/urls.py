from django.urls import path

from . import views

urlpatterns = [
    path("", views.projects_view, name="projects"),
    path("<str:primary_key>", views.project_view, name="project"),
    path("create", views.create_view, name="create"),
    path("<str:primary_key>/update", views.update_view, name="update"),
    path("<str:primary_key>/delete", views.delete_view, name="delete"),
]
