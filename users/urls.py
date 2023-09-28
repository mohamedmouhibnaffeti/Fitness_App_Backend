from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("signup/", Signup.as_view(), name="signup_endpoint" ),
    path("login/", Login.as_view(), name="Login"),
    path("list/", get_users.as_view(), name="List"),
    #path("jwt/access/", TokenObtainPairView.as_view(), name="Token_View"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="Token_Refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="Token_Verify")
]