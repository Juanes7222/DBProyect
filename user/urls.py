from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user),
    path("form/", views.forms),
    path("register/", views.register),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("exit/", views.exit, name="exit"),
    path("", views.home, name="home"),
    
]
