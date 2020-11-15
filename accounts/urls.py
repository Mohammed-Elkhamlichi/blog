# my Importing
from django.urls import path
from .views import (
    login_user,
    logout_user,
    register_user,
    profile,
)

# my App name:
app_name = "accounts"

# my Routes:
urlpatterns = [
    path("login/", login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    path('profile/<str:username>/', profile, name="profile"),
]