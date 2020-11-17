from django.contrib import admin
from .models import (
    Article,
    Category
)
# Register your models here.
# register the Article Model in the Admin View:
admin.site.register(Article)

# register the Category Model in the Admin View:
admin.site.register(Category)