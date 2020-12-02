from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Contact(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    site = models.URLField()
    message = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message + "sending by" + self.username)

    def get_absolute_url(self):
        return reverse('contact')
