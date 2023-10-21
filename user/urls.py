from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("form/", views.forms, name="form"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("psi-dashboard/", views.psi_dashboard, name="psi-dashboard"),
    path("exit/", views.exit, name="exit"),
    path("form_template/", views.forms, name="form_template"),
    path("exit/", views.exit, name="exit"),
    path("", views.home, name="home"),
    path("prueba/", views.prueba),
    path("forms_views/", views.forms_views, name="forms_views"),
    path("forms_views/get_message/<str:form_id>", views.get_message, name="get_message"),
    path("examples/", views.examples, name="examples"),
    path("guide/", views.guide, name="guide"),
    path("forms_views/download_wheels/", views.view_download_zip, name="download-zip"),
    path("integrations/", views.integrations, name="integrations"),
    path("integrations/integrate/", views.integrate, name="integrate"),
    path("get-integrations/", views.get_integrates, name="get-integrations"),
    path("view-integrations/<str:client_id>", views.view_info_user, name="view-integrations"),
    path("view-integrations/save-message/", views.save_message, name="save_message"),
    # path("get-integrations/download-zip-int", views.view_download_zip_int, name="download-zip-int"),
]
