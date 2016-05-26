from django.db import models
from django.conf import settings

from .sell import Sell


class Contact(models.Model):

    send = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="+",
    )

    accept = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="+",
    )
    message_text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    message_type = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return self.send.username + " to: " + self.accept.username
