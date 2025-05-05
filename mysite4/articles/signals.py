from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from .models import Article

@receiver(pre_save, sender=Article)
def create_slug(sender, instance, **kwargs):
    random_str = get_random_string(length=4)
    slug_base = f"{instance.title} {random_str}"
    instance.slug = slugify(slug_base)
