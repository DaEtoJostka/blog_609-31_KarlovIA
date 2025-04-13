from django.shortcuts import render
from .models import Article

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, article_id):
    data = {
        'id': article_id,
    }
    return render(request, 'articles/article_item.html', data)
