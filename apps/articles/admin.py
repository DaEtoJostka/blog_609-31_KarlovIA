from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date') # Fields to show in the list view
    exclude = ('slug',) # Hide slug from the edit/create form

admin.site.register(Article, ArticleAdmin) # Register with custom admin options
