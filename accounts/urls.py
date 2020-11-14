# my Importing
from django.urls import path
from .views import (
    login_user
)

# my App name:
app_name = "accounts"

# my Routes:
urlpatterns = [
    path("login/", login_user, name="login")
]