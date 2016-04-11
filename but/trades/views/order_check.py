from django.views.generic.detail import DetailView

from trades.models import Buy


class OrderCheckView(DetailView):

    model = Buy
    slug_field = "hash_id"
    template_name = "trades/order_check.html"
