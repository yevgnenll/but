from django.db import models

from django.conf import settings

from django.core.urlresolvers import reverse


class SellManager(models.Manager):

    def get_queryset(self):

        query = super(SellManager, self).get_queryset()

        return query.select_related(
                'user',
        )

    def is_public_true(self):

        query = self.get_queryset().filter(is_public=True)
        return query

    def is_public_false(self):

        query = self.get_queryset().filter(is_public=False)
        return query


class Sell(models.Model):

    objects = SellManager()

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
    )

    title = models.CharField(
            max_length=150,
    )

    sub_title = models.CharField(
            max_length=140,
    )
    goods_name = models.CharField(
            max_length=150,
    )

    stock = models.IntegerField(
            default=100,
    )

    sold_count = models.IntegerField(
            default=0,
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

    hash_id = models.CharField(
            max_length=20,
            null=True,
            blank=True,
            unique=True,
    )

    is_public = models.BooleanField(
            default=True,
    )

    created_at = models.DateTimeField(
            auto_now_add=True,
    )

    updated_at = models.DateTimeField(
            auto_now=True,
    )

    def get_absolute_url(self):

        return reverse(
                'goods_detail',
                kwargs={
                    'slug': self.hash_id,
                }
        )

    @property
    def left_stock(self):

        return self.stock - self.sold_count

    def __str__(self):
        return self.goods_name

    class Meta:
        verbose_name = "판매"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    sell_buy_set = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='sell_buy_set',
            through="Buy",
    )
