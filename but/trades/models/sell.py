from django.db import models

from django.conf import settings


class Sell(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
    )

    goods_name = models.CharField(
            max_length=150,
    )

    stock = models.IntegerField(
            default=100,
    )

    sold_count = models.IntegerField(
            default=100,
    )

    price = models.IntegerField(
            null=True,
            blank=True,
    )

    welcome_image = models.ImageField()

    sub_image = models.ImageField(
            null=True,
            blank=True,
    )

    second_image = models.ImageField(
            null=True,
            blank=True,
    )

    goods_description = models.TextField()
