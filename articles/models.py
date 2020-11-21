# my Importing:
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Category Model:
class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-updated']


# Article Model:
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to="artciles/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-updated']
