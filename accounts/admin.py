# my Importings:
from django.contrib import admin
from .models import (
    Profile,
    SendMessage
)

# Register your models here.

# register the User Profile Model:
admin.site.register(Profile)

# Register the Send Message Model:
admin.site.register(SendMessage)
