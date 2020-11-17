# my Importing
from django.urls import path
from .views import (
    login_user,
    logout_user,
    register_user,
    profile,
    contact_us,
)

# my App name:
app_name = "accounts"

# my Routes:
urlpatterns = [
    path("login/", login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    path('profile/', profile, name="profile"),
    path('contact/', contact_us, name='contact_us')
]