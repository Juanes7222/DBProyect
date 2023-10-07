from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("form/", views.forms, name="form"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("exit/", views.exit, name="exit"),
    # path("form_template/", views.form_template, name="form_template"),
    path("", views.home, name="home"),
    
]
