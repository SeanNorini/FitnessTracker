from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registration", views.registration, name="registration"),
    path("settings", views.settings, name="settings"),
    path("user_settings", views.user_settings, name="user_settings")
]