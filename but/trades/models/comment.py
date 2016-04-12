from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse


class CommentManager(models.Manager):

    def get_queryset(self):

        query = super(CommentManager, self).get_queryset()

        return query.select_related(
                'user',
        )


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
