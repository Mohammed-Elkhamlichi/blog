# my Importing:
from django .shortcuts import render
from django.http import HttpResponse
from django.template import loader
from articles.models import Article
from django.contrib.auth.decorators import login_required
# my Views:

# Home Page View:
def home(request):
    # QuerySet:
    latest_articles = Article.objects.all()[0:3]
    # Context:
    context = {
        "latest_articles":latest_articles,
    }
    # Template:
    template = loader.get_template('admins/home.html')
    return HttpResponse(template.render(context, request))


