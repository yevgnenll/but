from django.db.models.signals import post_save
from django.dispatch import receiver

from trades.models import Sell
from but.utils import make_hash


@receiver(post_save, sender=Sell)
def post_save_hashid(sender, instance, created, **kwargs):

    if not instance.hash_id:
        instance.hash_id = make_hash(instance)
        instance.save()
