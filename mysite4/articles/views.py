from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms # Import forms
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_item.html', {'article': article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:detail', slug=instance.slug)
    else:
        form = forms.ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.author != request.user:
        return HttpResponse('You are not authorized to edit this article.', status=403)
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', slug=article.slug)
    else:
        form = forms.ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form, 'article': article})

@login_required(login_url='/accounts/login/')
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.author != request.user:
        return HttpResponse('You are not authorized to delete this article.', status=403)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
