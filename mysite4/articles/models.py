from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
        
    def snippet(self):
        if len(self.body) > 50:
            return self.body[:50] + '...'
        return self.body
