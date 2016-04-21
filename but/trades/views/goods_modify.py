from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from trades.models import Sell
from .base import GoodsSellBase


class SellUpdateView(LoginRequiredMixin, GoodsSellBase, UpdateView):

    fields = [
        'title',
        'sub_title',
        'goods_name',
        'is_public',
        'stock',
        'price',
        'sub_image',
        'welcome_image',
        'second_image',
        'goods_description',
    ]

    template_name = "trades/goods_modify.html"
    slug_field = "hash_id"

    def form_valid(self, form):

        return super(SellUpdateView, self).form_valid(form)
