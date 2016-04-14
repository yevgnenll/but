from django.db import models
from django.conf import settings

from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class BuyManager(models.Manager):

    def get_queryset(self):

        query = super(BuyManager, self).get_queryset()
        return query.select_related(
                'user',
        )

    def is_complete_true(self):

        query = self.get_queryset().filter(is_complete=True)
        return query

    def is_complete_false(self):

        query = self.get_queryset().filter(is_complete=False)
        return query


class Buy(models.Model):

    objects = BuyManager()

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
            auto_now_add=True,
    )

    updated_at = models.DateTimeField(
            auto_now=True,
    )

    count = models.IntegerField(
            default=1,
    )

    price = models.IntegerField()

    address = models.CharField(
            max_length=255,
    )

    sell = models.ForeignKey(
            "Sell",
    )

    is_complete = models.BooleanField(
            default=False,
    )

    is_delete = models.BooleanField(
            default=False,
            # false is visible
    )

    hash_id = models.CharField(
            max_length=50,
    )

    @property
    def result_price(self):

        return self.price * self.count

    def get_absolute_url(self):

        return reverse(
            'buy_check', kwargs={
                'slug': self.hash_id,
            }
        )

    def __str__(self):

        return self.user.username + " has bought " + self.sell.title
