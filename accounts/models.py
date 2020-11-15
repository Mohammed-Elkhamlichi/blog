# my Importings:
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.

# User Profile Model:
class Profile(models.Model):
    ## user type:
    PERSON_TYPE = (
        ('w','women'),
        ('m','man'),
    )
    ## fields:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_birth = models.DateField(help_text='Required. Format: YYYY-MM-DD', null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=PERSON_TYPE, blank=True, null=True)
    image = models.ImageField(upload_to="accounts/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    # def __unicode__(self):
    #     return str(self.first_name)

    ## save informations:
    def save(self, *args, **kwargs):
        if not self.first_name:
            self.first_name = str(self.user.first_name)
        if not self.last_name:
            self.last_name = str(self.user.last_name)
        if not self.email:
            self.email = str(self.user.email)
        if not self.username:
            self.username = str(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    
    ## Meta class:
    class Meta:
        ordering = ['-updated']


def save_profile(sender, *rgs, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
post_save.connect(save_profile, sender=User)