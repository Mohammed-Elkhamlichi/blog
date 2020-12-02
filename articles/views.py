# my Importings:
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponseRedirect
)
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Article

# Create your views here.
latest_articles = Article.objects.all()[0:3]


# Articles View:
def articles(request):
    # QuerySet:
    articles = Article.objects.all()
    # Context:
    context = {
        "articles": articles,
        "latest_articles": latest_articles,
    }
    # Template:
    return render(request, 'articles/articles.html', context)


# Article Detail View:
def detail(request, id):
    # QuerySet:
    article = get_object_or_404(Article, id=id)
    # Context:
    context = {
        "article": article,
        "latest_articles": latest_articles,
    }
    # Template:
    template = loader.get_template('articles/detail.html')
    return HttpResponse(template.render(context, request))


# Article Search View:
def search(request):
    title = str(request.POST.get('title'))
    # QuerySet:
    articles = None
    # Form Validations:
    if request.method == "POST":
        title = str(request.POST.get('title'))
        print(title)
        articles = Article.objects.filter(content__contains=title)
        print(articles)
        if articles:
            messages.success(request, 'Articles Found')
        else:
            title = request.POST.get('title')
            messages.warning(request, 'Articles Found')
    # Context:
    context = {
        "latest_articles": latest_articles,
        "articles": articles,
    }
    # Template:
    return render(request, 'articles/search.html', context)
