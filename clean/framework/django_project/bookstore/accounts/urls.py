from django.urls import path
from .views import register, login, register_page, login_page, logout_page

urlpatterns = [
    # API
    path("api/register/", register),
    path("api/login/", login),

    # UI
    path("register/", register_page),
    path("login/", login_page),
    path("logout/", logout_page),
]
