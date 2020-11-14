from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import (
    LoginUserForm
)
# Create your views here.

def login_user(request):
    form = LoginUserForm()
    template = loader.get_template('accounts/login.html')
    context = {
        "form":form,
    }
    return HttpResponse(template.render(context, request))
    # or
    # return render(request, 'accounts/login.html', context)
