# my Importings:
from django.contrib import admin
from .models import Profile

# Register your models here.

# register the User Profile in the Admin View:
admin.site.register(Profile)
