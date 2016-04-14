from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import PhoneCertificate
from users.tasks import SendCertificateNumber


@receiver(post_save, sender=PhoneCertificate)
def post_save_cert_num(sender, instance, created, **kwargs):

    if created:
        task = SendCertificateNumber()
        task.delay(instance.id)
