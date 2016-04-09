from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.urlresolvers import reverse

from trades.models import Sell


class SellCreateView(LoginRequiredMixin, CreateView):

    model = Sell
    fields = [
       'goods_name',
       'stock',
       'price',
       'sub_image',
       'welcome_image',
       'second_image',
       'goods_description',
    ]

    template_name = "trades/register.html"

    success_url = "/"

    def form_valid(self, form):
        """
        automatically input user name
        """

        form.instance.user = self.request.user
        return super(SellCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print('form invalid --------')

        return super(SellCreateView, self).form_valid(form)
