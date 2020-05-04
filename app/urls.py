from django.urls import path, include
from .views import (
    UserSignupView,
    UserLoginView,
    UserLogoutView,
    PingView,
)
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("ping/", PingView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("signup/", UserSignupView.as_view()),
    path("logout/", UserLogoutView.as_view()),
]