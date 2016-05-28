from django.db import models
from django.contrib.auth.models import AbstractUser

from trades.models import Contact


class User(AbstractUser):

    phone_number = models.CharField(
        max_length=20,
    )

    profile_image = models.ImageField(
        null=True,
        blank=True,
    )

    description = models.TextField()

    is_phone_certificate = models.BooleanField(
        default=False,
    )

    is_email_certificate = models.BooleanField(
        default=False,
    )

    send_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name='accept_set',
        through=Contact,
        through_fields=('send', 'accept'),
    )

    def __str__(self):
        return self.username

    class Meta:

        verbose_name = "유저"
        verbose_name_plural = verbose_name
