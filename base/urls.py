from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("projects/", include("project.urls")),
    path("tasks/", include("task.urls")),
]