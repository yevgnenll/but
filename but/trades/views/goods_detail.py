from django.views.generic.detail import DetailView

from .base import GoodsSellBase


class GoodsDetailView(GoodsSellBase, DetailView):

    template_name = "trades/goods_detail.html"
    slug_field = "hash_id"
