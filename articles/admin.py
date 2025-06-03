from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # Fields to show in the list view
    list_display = ("title", "author", "date")
    # Hide slug from the edit/create form
    exclude = ("slug",)


# Register with custom admin options
admin.site.register(Article, ArticleAdmin)
