from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms # Import forms

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
        form = forms.CreateArticle(request.POST, request.FILES) # Added request.FILES
        if form.is_valid():
            # Save article to DB but don't commit yet
            instance = form.save(commit=False)
            # Assign the author
            instance.author = request.user
            # Now save to DB
            instance.save()
            return redirect('homepage') # Redirect to homepage
    else: # If GET request
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
