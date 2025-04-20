from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_item.html', {'article': article})
