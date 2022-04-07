from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    # Custom login url
    path("login/", views.log_in, name="login"),
    # Custom logout url
    path("logout/", views.log_out, name="logout"),
    # Registering a new user
    path("register/", views.register, name="register"),
]
