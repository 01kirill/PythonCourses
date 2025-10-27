from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def order_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"🛒 Новый заказ #{instance.id} от пользователя {instance.user.username} на сумму {instance.total} ₽")
