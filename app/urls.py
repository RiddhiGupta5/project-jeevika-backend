from django.urls import path, include
from .views import (
    UserSignupView,
    UserLoginView,
    UserLogoutView,
    UserDetailsView,
    PingView,
    OrganizationLogoutView,
    OrganizationRegisterView,
    OrganizationLoginView,
    OrganizationDetailsView,
)
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("ping/", PingView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("user/signup/", UserSignupView.as_view()),
    path("user/logout/", UserLogoutView.as_view()),
    path("user/details/", UserDetailsView.as_view()),
    path("org/login/", OrganizationLoginView.as_view()),
    path("org/signup/", OrganizationRegisterView.as_view()),
    path("org/logout/", OrganizationLogoutView.as_view()),
    path("org/details/", OrganizationDetailsView.as_view()),
]