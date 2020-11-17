# my Importings:
from django.urls import path
from .views import (
    articles,
    detail,
    search,
)

app_name='articles'


urlpatterns = [
    path('', articles, name="articles"),
    path('<int:id>/', detail, name='detail'),
    path('search/', search, name='search'),
]