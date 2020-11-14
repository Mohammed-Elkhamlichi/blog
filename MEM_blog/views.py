# my Importing:
from django .shortcuts import render
from django.http import HttpResponse
from django.template import loader

# my Views:

# Home Page View:
def home(request):
    template = loader.get_template('admins/home.html')
    context = {}
    return HttpResponse(template.render(context, request))