from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "portfolio"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("post/<int:pk>", views.PostView.as_view(), name="post"),
]
