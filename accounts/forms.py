# my Importings:
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# my Forms:
# User Profile Form:
class ProfileForm(forms.ModelForm):
    image = forms.ImageField(
        # label="",
        widget=forms.ClearableFileInput(
            attrs={
                "class":"col-md-12 p-2 border mt-2 rounded bg-warning",
                "placeholder":"Image Profile",
            }
        )
    )
    
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = list((
            'email','username','first_name','last_name','phone_number','image','type','country','bio',
        ))


# User Login Form:
class LoginUserForm(forms.ModelForm):
    # fields:
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class":"col-md-12 p-2 border rounded mt-3",
                "placeholder":"Username",
            }
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class":"col-md-12 p-2 border rounded mt-3",
                "placeholder":"Password",
            }
        )
    )

    # Meta class:
    class Meta:
        model = User
        fields = list(('username','password'))


# user register Form:
class RegisterUserForm(UserCreationForm):
    # fields:
    username = forms.CharField(
        label="",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"col-md-12 p-2 mt-2 mb-2 border rounded",
                "placeholder":"Username",
            }
        )
    )
    email = forms.CharField(
        label="",
        max_length=30,
        widget=forms.EmailInput(
            attrs={
                "class":"col-md-12 p-2 mt-2 mb-2 border rounded",
                "placeholder":"Email",
            }
        )
    )
    first_name = forms.CharField(
        label="",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"col-md p-2 mt-2 mb-2 border rounded",
                "placeholder":"First Name",
            }
        )
    )
    last_name = forms.CharField(
        label="",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"col-md p-2 mt-2 mb-2 border rounded",
                "placeholder":"Last Name",
            }
        )
    )
    password1 = forms.CharField(
        label="",
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class":"col-md-12 p-2 mt-2 mb-2 border rounded",
                "placeholder":"Password",
            }
        )
    )
    password2 = forms.CharField(
        label="",
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class":"col-md-12 p-2 mt-2 mb-2 border rounded",
                "placeholder":"Password confirmation",
            }
        )
    )
    # Meta class:
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    # clean fields:
    ## clean Username:
    def clean_username(self, *args, **kwargs):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('Username is already exists')
        else:
            return cd['username']

    ## clean Email:
    def clean_email(self, *args, **kwargs):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('Email is already ewists')
        else:
            return cd['email']