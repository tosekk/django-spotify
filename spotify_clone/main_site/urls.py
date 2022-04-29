from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path("", views.homepage, name="home-page"),
    path("premium/", views.premium, name="premium-page"),
    path("download/", views.download, name="download-page"),
    path("account/", views.account, name="account-page"),
    path("signup/", views.SignUpView.as_view(), name="sign-up-page"),
    path("login/", views.login, name="log-in-page"),
    path("support/", views.support, name="support-page"),
]