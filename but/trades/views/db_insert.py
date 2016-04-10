from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from trades.models import Sell
from .base import GoodsSellBase


class SellCreateView(LoginRequiredMixin, GoodsSellBase,  CreateView):

    fields = [
       'title',
       'sub_title',
       'goods_name',
       'stock',
       'price',
       'sub_image',
       'welcome_image',
       'second_image',
       'goods_description',
    ]

    template_name = "trades/register.html"

    def form_valid(self, form):
        """
        automatically input user name
        """

        form.instance.user = self.request.user
        return super(SellCreateView, self).form_valid(form)
