from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from trades.models import Buy, Sell


class OrderPageView(LoginRequiredMixin, CreateView):

    model = Buy
    template_name = "trades/order_page.html"

    fields = [
            'count',
    ]

    def form_valid(self, form):

        slug = self.kwargs.get('slug')
        sell_product = Sell.objects.get(hash_id=slug)

        form.instance.user = self.request.user
        form.instance.sell = sell_product
        form.instance.price = sell_product.price

        return super(OrderPageView, self).form_valid(form)
