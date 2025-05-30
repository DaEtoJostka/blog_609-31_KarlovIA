from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms # Import forms
from django.http import HttpResponse


def article_list(request):
    """Displays a list of all articles, ordered by date."""
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_item(request, slug):
    """Displays a single article item identified by its slug."""
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_item.html', {'article': article})


@login_required(login_url='/accounts/login/')
def article_create(request):
    """Handles creation of a new article. Requires login."""
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
    """Handles updating an existing article. Requires login and authorship."""
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
    """Handles deletion of an article. Requires login and authorship.
    Displays a confirmation page on GET, deletes on POST."""
    article = get_object_or_404(Article, slug=slug)
    if article.author != request.user:
        return HttpResponse('You are not authorized to delete this article.', status=403)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
