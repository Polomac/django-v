from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from rest_framework import viewsets
from django.urls import reverse

from .serializers import ArticleSerializer

# Create your views here.
def article_list(request):
  articles = Article.objects.all()
  return HttpResponse(articles)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('date')
    serializer_class = ArticleSerializer