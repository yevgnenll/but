from django.views.generic.detail import DetailView

from .base import GoodsSellBase


class GoodsDetailView(GoodsSellBase, DetailView):

    template_name = "trades/goods_detail.html"
    slug_field = "hash_id"

    def dispatch(self, request, *args, **kwargs):

        # from IPython import embed; embed()

        return super(GoodsDetailView, self).dispatch(request, args, kwargs)
