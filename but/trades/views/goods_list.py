from django.views.generic.list import ListView
from trades.models import Sell
from .base import GoodsSellBase


class GoodsListView(GoodsSellBase, ListView):

    template_name = "trades/goods_list.html"
    queryset = Sell.objects.filter(
            is_public=True
            ).order_by('-created_at')
