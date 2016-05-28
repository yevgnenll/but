from django.db.models.signals import post_save
from django.dispatch import receiver

from trades.models import Sell, Buy, Contact
from but.utils import make_hash
from trades.tasks import SendEmailBuyerToSeller


@receiver(post_save, sender=Sell)
@receiver(post_save, sender=Buy)
def post_save_hashid(sender, instance, created, **kwargs):

    if not instance.hash_id:
        instance.hash_id = make_hash(instance)
        instance.save()


@receiver(post_save, sender=Buy)
def post_save_count_apply(sender, instance, created, **kwargs):

    if created:
        sell = instance.sell
        sell.stock -= instance.count
        if sell.stock == 0:
            sell.is_public = False
        sell.save()


@receiver(post_save, sender=Contact)
def post_save_contact(sender, instance, created, **kwargs):

    if created:
        task = SendEmailBuyerToSeller()
        task.delay(instance.id)
