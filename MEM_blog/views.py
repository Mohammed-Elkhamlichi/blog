# my Importing:
from django .shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# my Views:

# Home Page View:
@login_required()
def home(request):
    template = loader.get_template('admins/home.html')
    context = {}
    return HttpResponse(template.render(context, request))