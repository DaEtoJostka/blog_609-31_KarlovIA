from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    """Represents a blog article or a similar piece of content."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        """Returns a short snippet of the article body."""
        if len(self.body) > 50:
            return self.body[:50] + '...'
        return self.body
