from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse


class CommentManager(models.Manager):

    def get_queryset(self):

        query = super(CommentManager, self).get_queryset()

        return query.select_related(
                'user',
        )

    def is_public_true(self):

        query = self.get_queryset().filter(is_public=True)
        return query

    def is_public_false(self):

        query = self.get_queryset().filter(is_public=False)
        return query


class Comment(models.Model):

    objects = CommentManager()

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
    )

    sell = models.ForeignKey(
            "Sell",
    )

    content = models.CharField(
            max_length=255,
    )

    created_at = models.DateTimeField(
            auto_now_add=True,
    )

    updated_at = models.DateTimeField(
            auto_now=True,
    )

    is_public = models.BooleanField(
            default=True,
    )

    def get_absolute_url(self):

        return revsere(
                'goods_detail', kwargs={
                    'slug': self.sell.hash_id,
                }
        )

    def __str__(self):

        return self.content + " by @" + self.user.username
