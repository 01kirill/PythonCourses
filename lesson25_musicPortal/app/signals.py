from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Song
from django.core.cache import cache
from .views import CACHE_SONGS_KEY


@receiver(post_save, sender=Song)
@receiver(post_delete, sender=Song)
def clear_songs_cache(sender, **kwargs):
    cache.delete(CACHE_SONGS_KEY)
