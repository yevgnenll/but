from django.views.generic.list import ListView
from .base import GoodsSellBase


class GoodsListView(GoodsSellBase, ListView):

    template_name = "trades/goods_list.html"
